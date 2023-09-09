import os

import torch 

torch.cuda.empty_cache()

################# RUN VID SINGLE ####################

command_list = [
    "python", "./main.py",
    # "--pretrainedmodel", "./pretrained_checkpoints/checkpoint0005.pth",            
    "--backbone", "swin_b_p4w7",
    "--epochs", "35",
    "--num_feature_levels", "1", 
    "--num_queries", "100", 
    "--hidden_dim", "256",
    "--dilation",
    "--batch_size", "4", 
    # "--num_ref_frames", "2", 
    "--num_classes", "4",
    "--img_side", "600", 
    "--resume" , "/home/ubuntu/priy_dev/TransVOD/TransVOD_Lite/pretrained/single/checkpoint0006.pth",
    "--lr_drop_epochs", "21",
    "--num_workers", "24",
    "--with_box_refine",
    "--coco_pretrain",
    "--dataset_file", "vid_single",
    "--output_dir", "./experiments/UAV_single_vid_id_15/" ,
    "--data_root", "/home/ubuntu/priy_dev/Datasets/UAV",
    # "--freeze_backbone",
            ]


command = ' '.join(command_list)

os.system(command)


