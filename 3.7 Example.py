# -*- coding: utf-8 -*-

#3.7 - generate a sine with a sampling frequency of 100 Hz. 
#      The sampling starts at t0=1 and ends at t1=2
#      Amplitude is 2, frequency is 5, phase is 0. Plot the signal and the envelope.

import numpy as np
import matplotlib.pyplot as plt
def mySin(A,freq,phase,t):
    y=A*np.sin(2*np.pi*freq*t+phase)
    return y

fs=100
t=np.arange(1, 2, 1/fs)
A=2
freq=5
phase=0
x=mySin(A,freq,phase,t)

plt.figure()
plt.plot(x)


