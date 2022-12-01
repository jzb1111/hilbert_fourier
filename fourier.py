# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 21:49:57 2022

@author: asus
"""

import numpy as np
import matplotlib.pyplot as plt

'''alis=[i for i in range(100)]

im=np.zeros((200,200))

for i in range(len(alis)):
    q=alis[i]*np.exp(2*np.pi*(i/len(alis))*1j*1)
    chang=int(q.real-100)
    kuan=int(q.imag-100)
    im[chang][kuan]=1
plt.figure(0)
plt.imshow(im)
'''

def fourier_fit(lis,f_n):
    #lis:曲线的点集lis={p0,p1,p2...},p0=[x0,y0],...
    #f_n:级数的长度
    f_num=[0]
    f_num+=[i+1 for i in range(f_n)]
    f_num+=[-i-1 for i in range(f_n)]
    f_num=sorted(f_num)
    res=[]
    for i in range(len(f_num)):
        fnum=f_num[i]
        count=0+0j
        countlis=[]
        for j in range(len(lis)):
            weight=np.exp(-2*np.pi*fnum*(j/len(lis))*1j)
            count+=weight*lis[j]
            #print(count)
            countlis.append(count)
        #print(np.mean(countlis))
        res.append(count/len(lis))
    return res

def Dfourier(flis,rough=100):
    fn=len(flis)//2
    f_num=[0]
    f_num+=[i+1 for i in range(fn)]
    f_num+=[-i-1 for i in range(fn)]
    f_num=sorted(f_num)
    
    res=[]
    
    for i in range(rough):
        tmp=0+0j
        for j in range(len(f_num)):
            f_k=f_num[j]
            weight=np.exp(2*np.pi*f_k*(i/rough)*1j)
            tmp+=weight*flis[j]
        res.append(tmp)
    return res