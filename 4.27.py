# -*- coding: utf-8 -*-

#4.27 - Represent the amplitude variation, magnitutde and phase spectrums for
#       the Rectangular Pulse waveform

import numpy as np
import matplotlib.pyplot as plt

def rectangularPulse(A, tStart, tEnd, t0,t1):
    y=[]
    time=np.arange(t0,t1, 1/100)
    for x in time:
        if x>tStart and x<tEnd:
            y.append(A)
        else:
            y.append(0)
            
    #time domain       
    plt.figure()
    plt.plot(time, y)            
    plt.xlabel('time')
    plt.ylabel('amplitude')
    
    #magnitude plot
    Y=np.fft.fft(y)
    plt.figure()
    plt.xlabel('index')
    plt.ylabel('magnitude')
    plt.plot(abs(Y))             
    
    #phase spectrum
    plt.figure()
    plt.xlabel('Frequency')
    plt.ylabel('Phase (Radians)') 
    plt.phase_spectrum(y)        

plt.close('all')    
rectangularPulse(2, 6, 7, -1, 20)