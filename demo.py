# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 21:58:33 2022

@author: asus
"""

from utils import load_image,im2gray
from hilbert_fourier import mat2hilbert_fourier_series,hilbert_fourier_series2mat
import matplotlib.pyplot as plt
import numpy as np

from fourier import fourier_fit,Dfourier

im=load_image('000215.jpg')
gray=im2gray(im)

'''im=np.zeros((16,16))
for i in range(16):
    for j in range(16):
        if (i-8)**2+(j-8)**2<50:
            im[i][j]=1'''
plt.figure(0)
plt.imshow(gray)

fs=mat2hilbert_fourier_series(gray,200)
df=hilbert_fourier_series2mat(fs,8)
df=np.abs(df)
plt.figure(1)
plt.imshow(df)

'''gray_flat=np.reshape(gray,[-1])
fsf=fourier_fit(gray_flat, 200)
dfsf=Dfourier(fsf,256*256)
dfsf=np.reshape(np.abs(dfsf),[256,256])
plt.figure(2)
plt.imshow(dfsf)'''