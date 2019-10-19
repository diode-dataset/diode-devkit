# DIODE: A Dense Indoor and Outdoor DEpth Dataset


DIODE (Dense Indoor/Outdoor DEpth) is a dataset that contains diverse high-resolution color images with accurate, dense, and far-range depth measurements. DIODE is the first public dataset to include **RGBD images of indoor and outdoor scenes obtained with one sensor suite**.

Refer to our [homepage](https://diode-dataset.org) and [technical report](https://arxiv.org/abs/1908.00463) for more details.

### Dataset Download
We have released the train and validation splits of DIODE depth and DIODE normal, including RGB images, depth maps, depth validity masks and surface normal maps. Test set is coming soon.

**Download links:**

1. **DIODE Depth** (RGB images, Depth maps and Depth validity masks):

|     Partition      |                      Amazon Web Service                      | Tencent Cloud Service                                               |             MD5 Hash             |
| :----------------: | :----------------------------------------------------------: | :------------------------------------------------------------: | :------------------------------: |
|    Train (81GB)    | [train.tar.gz](http://diode-dataset.s3.amazonaws.com/train.tar.gz) | [train.tar.gz](https://diode-dataset-1254389886.cos.ap-shanghai.myqcloud.com/train.tar.gz) | 3a94632398fe1d002d89f11743f748b1 |
| Validation (2.6GB) | [val.tar.gz](http://diode-dataset.s3.amazonaws.com/val.tar.gz) | [val.tar.gz](https://diode-dataset-1254389886.cos.ap-shanghai.myqcloud.com/val.tar.gz) | 5c895d09201b88973c8fe4552a67dd85 |

2. **DIODE Normal** (Normal maps only):

|     Partition      |                      Amazon Web Service                      | Tencent Cloud Service                                               |             MD5 Hash             |
| :----------------: | :----------------------------------------------------------: | :------------------------------------------------------------: | :------------------------------: |
|    Train (126GB)    | [train_normals.tar.gz](http://diode-dataset.s3.amazonaws.com/train_normals.tar.gz) | [train_normals.tar.gz](https://diode-dataset-1254389886.cos.ap-shanghai.myqcloud.com/train_normals.tar.gz) | 9c0617ebe1eaf1928fdf3344e1c42aef |
| Validation (4.6GB) | [val_normals.tar.gz](http://diode-dataset.s3.amazonaws.com/val_normals.tar.gz) | [val_normals.tar.gz](https://diode-dataset-1254389886.cos.ap-shanghai.myqcloud.com/val_normals.tar.gz) | 323ccaf60abebdb59705dcd8b529d709 |

### Dataset Layout
DIODE data is organized hierarchically. Detailed structure is shown as follows:
![Layout](dataset_layout.png)

### File Naming Conventions and Formats
The dataset consists of RGB images, depth maps, depth validity masks and surface normal maps. Their formats are as follows:

  RGB images (`*.png`): RGB images with a resolution of 1024 × 768.

  Depth maps (`*_depth.npy`): Depth ground truth with the same resolution as the images.

  Depth validity masks (`*_depth_mask.npy`): Binary depth validity masks where 1 indicates valid sensor returns and 0 otherwise.
  
  Surface normals maps (`*_normal.npy`): Surface normal vector ground truth with the same resolution as the images. Invalid normals are represented as (0,0,0).

### Devkit
This development toolkit contains:
1. A json file that enumerates the data in DIODE. The layout of this file is explained in diode.py. It serves as the single point of reference during dataloading.
2. A sample pytorch data loading module.
3. A jupyter-notebook demo showcasing data loading, metadata querying and depth visualization.
4. A text file documenting camera intrinsics. 
5. A python file for computation of metrics using numpy. 


### Citation
```
@article{diode_dataset,
    title={{DIODE}: {A} {D}ense {I}ndoor and {O}utdoor {DE}pth {D}ataset},
    author={Igor Vasiljevic and Nick Kolkin and Shanyi Zhang and Ruotian Luo and 
            Haochen Wang and Falcon Z. Dai and Andrea F. Daniele and Mohammadreza Mostajabi and 
            Steven Basart and Matthew R. Walter and Gregory Shakhnarovich},
    year = {2019}
    journal={CoRR},
    volume={abs/1908.00463},
    year = {2019},
    url={http://arxiv.org/abs/1908.00463}
}
```
### Contact
If you have any questions, please contact us at [diode.dataset@gmail.com](diode.dataset@gmail.com).
