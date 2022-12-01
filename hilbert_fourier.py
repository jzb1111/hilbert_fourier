# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 19:07:41 2022

@author: asus
"""

import numpy as np
from hilbert import gen_hilbert_curve
from fourier import fourier_fit,Dfourier
from utils import gather,line_gather

def mat2hilbert_fourier_series(mat,f_num=20):
    
    hilbert_curve=gen_hilbert_curve(int(np.log2(len(mat))))
    hilbert_mat=gather(mat,hilbert_curve)
    f_series=fourier_fit(hilbert_mat,f_num)
    return f_series

def hilbert_fourier_series2mat(hilbert_fourier_series,hilbert_num=3):
    #res=np.zeros((2**hilbert_num))
    df=Dfourier(hilbert_fourier_series,(2**hilbert_num)**2)
    #print(len(df))
    df=np.reshape(df,[int((2**hilbert_num)),int((2**hilbert_num))])
    hilbert_curve=gen_hilbert_curve(hilbert_num)
    df=line_gather(df,hilbert_curve)
    #res=gather(df,hilbert_curve)
    #res=np.reshape(res,[2**hilbert_num,2**hilbert_num])
    return df