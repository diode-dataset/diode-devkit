import os.path as osp
from itertools import chain
import json

from torch.utils.data import Dataset
import numpy as np
from PIL import Image

import matplotlib.pyplot as plt

'''
The json metadata for DIODE is laid out as follows:
train:
    outdoor:
        scene_000xx:
            scan_00yyy:
                - 000xx_00yyy_indoors_300_010
                - 000xx_00yyy_indoors_300_020
                - 000xx_00yyy_indoors_300_030
        scene_000kk:
            _analogous_
val:
    _analogous_
test:
    _analogous_
'''

_VALID_SPLITS = ('train', 'val', 'test')
_VALID_SCENE_TYPES = ('indoors', 'outdoor')


def check_and_tuplize_tokens(tokens, valid_tokens):
    if not isinstance(tokens, (tuple, list)):
        tokens = (tokens, )
    for split in tokens:
        assert split in valid_tokens
    return tokens


def enumerate_paths(src):
    '''flatten out a nested dictionary into an iterable
    DIODE metadata is a nested dictionary;
    One could easily query a particular scene and scan, but sequentially
    enumerating files in a nested dictionary is troublesome. This function
    recursively traces out and aggregates the leaves of a tree.
    '''
    if isinstance(src, list):
        return src
    elif isinstance(src, dict):
        acc = []
        for k, v in src.items():
            _sub_paths = enumerate_paths(v)
            _sub_paths = list(map(lambda x: osp.join(k, x), _sub_paths))
            acc.append(_sub_paths)
        return list(chain.from_iterable(acc))
    else:
        raise ValueError('do not accept data type {}'.format(type(src)))


def plot_depth_map(dm, validity_mask):
    validity_mask = validity_mask > 0
    MIN_DEPTH = 0.5
    MAX_DEPTH = min(300, np.percentile(dm, 99))
    dm = np.clip(dm, MIN_DEPTH, MAX_DEPTH)
    dm = np.log(dm, where=validity_mask)

    dm = np.ma.masked_where(~validity_mask, dm)

    cmap = plt.cm.jet
    cmap.set_bad(color='black')
    plt.imshow(dm, cmap=cmap, vmax=np.log(MAX_DEPTH))


def plot_normal_map(normal_map):
    normal_viz = normal_map[:, ::, :]

    normal_viz = normal_viz + np.equal(np.sum(normal_viz, 2, 
    keepdims=True), 0.).astype(np.float32)*np.min(normal_viz)

    normal_viz = (normal_viz - np.min(normal_viz))/2.
    plt.axis('off')
    plt.imshow(normal_viz)

    
    
class DIODE(Dataset):
    def __init__(self, meta_fname, data_root, splits, scene_types):
        self.data_root = data_root
        self.splits = check_and_tuplize_tokens(
            splits, _VALID_SPLITS
        )
        self.scene_types = check_and_tuplize_tokens(
            scene_types, _VALID_SCENE_TYPES
        )
        with open(meta_fname, 'r') as f:
            self.meta = json.load(f)

        imgs = []
        for split in self.splits:
            for scene_type in self.scene_types:
                _curr = enumerate_paths(self.meta[split][scene_type])
                _curr = map(lambda x: osp.join(split, scene_type, x), _curr)
                imgs.extend(list(_curr))
        self.imgs = imgs

    def __len__(self):
        return len(self.imgs)

    def __getitem__(self, index):
        im = self.imgs[index]
        im_fname = osp.join(self.data_root, '{}.png'.format(im))
        de_fname = osp.join(self.data_root, '{}_depth.npy'.format(im))
        de_mask_fname = osp.join(self.data_root, '{}_depth_mask.npy'.format(im))

        im = np.array(Image.open(im_fname))
        de = np.load(de_fname).squeeze()
        de_mask = np.load(de_mask_fname)
        return im, de, de_mask
