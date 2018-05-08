# -*- coding: utf-8 -*-

#6.4 - We will use a matched filter to extract tiangular signals mingled with a sinusoid and noise. 
#      The matched filter template will have also triangular form, with similar, but different values. 
#      After a high pass filtering we obtain the triangular waveforms, with delays because of the filtering.

import numpy as np
import matplotlib.pyplot as plt

def rPulse(A, tStart, tEnd, time):
    y=[]
    for x in time:
        if x>tStart and x<tEnd:
            y.append(A)
        else:
            y.append(0)
    return y

fs=200
t0=0
tf=3
t=np.arange(t0,tf,1/fs)

t1=0
t2=1.5
t3=2
dt=0.1

a=rPulse(3, t1, t1+dt, t)
b=rPulse(3,t2,t2+dt,t)
c=rPulse(3,t3,t3+dt,t)
x=[a[i]+b[i]+c[i] for i in range(len(a))]
plt.figure('Original Signal')
plt.plot(t,x)



