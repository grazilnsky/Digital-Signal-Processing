# -*- coding: utf-8 -*-

#3.53 - Write your own primitives for 7 other important waveforms

import numpy as np
import matplotlib.pyplot as plt

#A=amplitude
#P=period
#t=interval of time

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
    
    
plt.close('all')

t0=-8*np.pi #start time
t1=8*np.pi #end time
fs=100   #fs=sampling frequency
t=np.arange(t0, t1, 1.0/fs)
chirp_fStart=1  #starting frequency of chirp
chirp_fEnd=5   #end frequency of chirp


plt.figure('Sawtooth')
plt.plot(t, mySawtooth(1,1,t))
plt.show()

plt.figure('Square')
plt.plot(t, mySquare(1,1,t))
plt.show()
    
plt.figure('Triangle')
plt.plot(t, myTriangle(1,1,t))
plt.show()
    
plt.figure('Cardinal Sin')
plt.plot(t, mySinc(t))
plt.show()

plt.figure('Normalized Cardinal Sin')
plt.plot(t, myNormalizedSinc(t))
plt.show()

plt.figure('Exponential Chirp')
plt.plot(t, myExponentialChirp(1,10,chirp_fStart, chirp_fEnd,t))
plt.show()

plt.figure('Gauss')
plt.plot(t, myGaussianBell(1,7,0.3,t))
plt.show()