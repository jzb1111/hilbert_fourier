# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 19:11:28 2022

@author: asus
"""

import numpy as np

def gen_hilbert_curve(n):
    
    if n==1:
        return gen_hilbert_unit()
    else:
        level=gen_level(n)
        zero=np.zeros((level,level))
        left_down_max=0
        left_up_max=(level//2)**2
        right_up_max=((level//2)**2)*2
        right_down_max=((level//2)**2)*3
        #print(zero[0:level//2,0:level//2])
        hilbert_tmp=gen_hilbert_curve(n-1)
        zero[0:level//2,0:level//2]=hilbert_tmp+left_up_max#左上 
        zero[0:level//2,level//2:]=hilbert_tmp+right_up_max#右上
        zero[level//2:,0:level//2]=mat_rot_main(hilbert_tmp)+left_down_max#左下 
        zero[level//2:,level//2:]=mat_rot_sub(hilbert_tmp)+right_down_max#右下
    
    return zero

def gen_level(n):
    if n==1:
        return 2 
    return gen_level(n-1)*2

def gen_hilbert_unit():
    res=[[1,2],[0,3]]
    return np.array(res)

def mat_rot_sub(mat):
    zero=np.zeros_like(mat)
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            new_ind=[j,i]
            zero[new_ind[0]][new_ind[1]]=mat[i][j]
    return zero

def mat_rot_main(mat):
    zero=np.zeros_like(mat)
    #print(mat)
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            new_ind=[len(mat[i])-j-1,len(mat)-i-1]
            #print(new_ind)
            zero[new_ind[0]][new_ind[1]]=mat[i][j]
    return zero