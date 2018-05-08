# -*- coding: utf-8 -*-

#functions from 3.53

import numpy as np

def mySawtooth(A, P, t):
    y=-(2*A/np.pi)*(np.arctan(1/np.tan(np.pi*t/P)))
    return y

def mySquare(A, P, t):
    y=np.sign(np.sin(t/P))
    return y
    

def myTriangle(A,P,t):
    y=2*np.abs((2*A/np.pi)*(np.arctan(1/np.tan(np.pi*t/P))))-1
    return y
    
def mySinc(t):
    y=np.sin(t)/t
    return y
    
def myNormalizedSinc(t):
    y=np.sin(np.pi*t)/(np.pi*t)
    return y
    
def myExponentialChirp(A, P, start, end, t):
    k=(end/start)**(1/P)
    y=np.sin(2*np.pi*start*(np.power(k,(t-P))-1)/np.log(k))
    return y
  
def myGaussianBell(a,b,c,t):
    y=a*np.power(np.e, -(np.power((t-b), 2)/2*np.power(c,2)))
    return y