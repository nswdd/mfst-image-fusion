# mfst-image-fusion
MFST: Multi-Modal Feature Self-Adaptive Transformer for Infrared and Visible Image Fusion

## Requirements
```
pytorch==1.7.0
scipy==1.2.0
```
## Models
[models](https://pan.baidu.com/s/1KIxKjylZkzHoZRpQGRe3SQ?pwd=q4k5)
## Datasets
[TNO dataset](https://pan.baidu.com/s/1mNae9WHdEVo1TVyv2pou1Q?pwd=jg0i)
## Demo
```
python test_21pairs.py
```
## Citing
```
@Article{rs14133233,
  AUTHOR = {Liu, Xiangzeng and Gao, Haojie and Miao, Qiguang and Xi, Yue and Ai, Yunfeng and Gao, Dingguo},
  TITLE = {MFST: Multi-Modal Feature Self-Adaptive Transformer for Infrared and Visible Image Fusion},
  JOURNAL = {Remote Sensing},
  VOLUME = {14},
  YEAR = {2022},
  NUMBER = {13},
  ARTICLE-NUMBER = {3233},
  URL = {https://www.mdpi.com/2072-4292/14/13/3233},
  ISSN = {2072-4292},
  ABSTRACT = {Infrared and visible image fusion is to combine the information of thermal radiation and detailed texture from the two images into one informative fused image. Recently, deep learning methods have been widely applied in this task; however, those methods usually fuse multiple extracted features with the same fusion strategy, which ignores the differences in the representation of these features, resulting in the loss of information in the fusion process. To address this issue, we propose a novel method named multi-modal feature self-adaptive transformer (MFST) to preserve more significant information about the source images. Firstly, multi-modal features are extracted from the input images by a convolutional neural network (CNN). Then, these features are fused by the focal transformer blocks that can be trained through an adaptive fusion strategy according to the characteristics of different features. Finally, the fused features and saliency information of the infrared image are considered to obtain the fused image. The proposed fusion framework is evaluated on TNO, LLVIP, and FLIR datasets with various scenes. Experimental results demonstrate that our method outperforms several state-of-the-art methods in terms of subjective and objective evaluation.},
  DOI = {10.3390/rs14133233}
}
```