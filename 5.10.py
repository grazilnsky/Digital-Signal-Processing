# -*- coding: utf-8 -*-

#5.10 - Write a function that will compute the circulant matrix C
#       corresponding to the vector x

import numpy as np

def circulant(x):
    C=x
    for i in range((len(x[0]))-1):
        newrow=np.roll(x,i+1)    #roll the array one position to the right
        C=np.concatenate((C, newrow), axis=0)  #concatenate that to the matrix
    print(C)
    
x=np.array([[1,2,3,4,5,6]]) 
circulant(x)  
