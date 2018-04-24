# MegaDepth: Learning Single-View Depth Prediction from Internet Photos
===========================

This is an code of the algorithm described in "MegaDepth: Learning Single-View Depth Prediction from Internet Photos, Z. Li and N. Snavely, CVPR 2018". The code skeleton is based on "https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix". If you use our code or models for academic purposes, please consider citing:

    @inproceedings{MDLi18,
	  	title={MegaDepth: Learning Single-View Depth Prediction from Internet Photos},
	  	author={Zhengqi Li and Noah Snavely},
	  	booktitle={Computer Vision and Pattern Recognition (CVPR)},
	  	year={2018}
	}


#### Dependencies:
* The code was written in Pytorch and Python 2.7, but it should be easy to adapt it to Python 3 version if needed.
* You might need skimage, h5py libraries installed for python before running the code.


#### Evaluation on the MegaDepth test splits:
* Download MegaDepth dataset from http://www.cs.cornell.edu/projects/megadepth/.
* Download pretrained model (specific for MD dataset) from ??? and put it in "checkpoints/test_local/best_vanila_net_G.pth" 
* Download test list files from ???, it should include two subfolders corresponding to images with landscape and portrait orientations.
* To compute scale invarance RMSE on MD testset, change the variable "dataset_root" in python file "rmse_error_main.py" to the root directory of MegaDepth_v1 folder, and change variable "test_list_dir_l" and "test_list_dir_p" to corresponding paths of test lists of images with landscape and portrait orientations, and run:
```bash
    python rmse_error_main.py
```
* To compute Structure from Motion Disagreement Rate (SDR), change the variable "dataset_root" in python file "rmse_error_main.py" to the root directory of MegaDepth_v1 folder, and change variable "test_list_dir_l" and "test_list_dir_p" to corresponding paths of test lists of images with landscape and portrait orientations, and run:
```bash
    python SDR_compute.py
```
* If you want to run our model on arbitrary Internet photos, please download pretrained model from ???, which has much better generalization ability (qualitatively speaking) to completely unknown scenes.

