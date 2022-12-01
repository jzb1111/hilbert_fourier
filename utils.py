# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 21:53:59 2022

@author: asus
"""

import cv2
import numpy as np

def load_image(imageurl,size=(256,256)):#加载vgg模型必须这样加载图像
    im = cv2.resize(cv2.imread(imageurl),size).astype(np.float32)
    return im

def im2gray(im):
    gray=np.zeros((len(im),len(im[0])))
    for i in range(len(im)):
        for j in range(len(im[i])):
            gray[i][j]=np.mean(im[i][j])
    return gray

def gather(mat,index):
    tmp=np.stack([mat,index],axis=-1)
    tmp=np.reshape(tmp,[-1,2])
    sort_tmp=sorted(tmp,key=lambda x:x[1])
    res=[]
    for i in range(len(sort_tmp)):
        res.append(sort_tmp[i][0])
    return res

def line_gather(line,index):
    tmp=np.zeros_like(index)
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            tmp[i][j]=i*len(tmp)+j
    
    line=np.reshape(line,[-1,1])
    
    tmp=np.stack([tmp,index],axis=-1)
    tmp=np.reshape(tmp,[-1,2])
    tmp=sorted(tmp,key=lambda x:x[1])
    #print(line.shape)
    #print(len(tmp),len(tmp[0]))
    tmp=np.concatenate([line,tmp],axis=-1)
    tmp=sorted(tmp,key=lambda x:x[1])
    
    res=np.zeros((int(len(tmp)**0.5),int(len(tmp)**0.5)))
    for i in range(len(res)):
        for j in range(len(res[i])):
            res[i][j]=np.abs(tmp[i*len(res)+j][0])
    return res