#!/usr/bin/python
#-*-coding:UTF-8-*-
# Import the converted model's class
import os
import re
import tensorflow as tf
from  tensorflow.python import pywrap_tensorflow

dataFoldPath='/media/john/磁盘阵列1/flownet2_data/PoseNetData/'
path = dataFoldPath+'posenet_weight/KingsCollege/'
preResPath=path+'181123/'
preTrainModelFile='PoseNet_25000.ckpt'
meta_file='PoseNet_25000.ckpt.meta'
ckpt_file1='PoseNet_25000.ckpt'

model_exp=preResPath+preTrainModelFile

def get_model_filenames(model_dir):
    files=os.listdir(model_dir)
    meta_files=[s for s in files if s.endswith('.meta')]
    if len(meta_files)==0:
        raise ValueError('No .meta files (%s)'%model_dir)

    meta_file=meta_files[0]
    ckpt=tf.train.get_checkpoint_state(model_dir)
    if ckpt and ckpt.model_checkpoint_path:
        ckpt_file=os.path.basename(ckpt.model_checkpoint_path)
        return meta_file,ckpt_file




def main():
    #meta_file,ckpt_file=get_model_filenames(preResPath)


    print('Metagraph file: %s'%meta_file)
    print('Checkpoint file: %s'% ckpt_file1)
    #ckpt_file=os.path.join(preResPath,ckpt_file)
    ckpt_file=preResPath+ckpt_file1
    reader=pywrap_tensorflow.NewCheckpointReader(ckpt_file)
    var_to_shape_map=reader.get_variable_to_shape_map()

    for key in var_to_shape_map:
        print("tensor_name: ",key)

    with tf.Session() as sess:
        saver=tf.train.import_meta_graph(os.path.join(preResPath,meta_file))
        saver.restore(tf.get_default_session(),
                      os.path.join(preResPath,ckpt_file))
        print(sess.run('cls1_fc_pose_xyz:0'))




if __name__ == '__main__':
	main()