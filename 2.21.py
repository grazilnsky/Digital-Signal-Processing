# -*- coding: utf-8 -*-

#2.21 - Plot three sine functions with the phase difference of 2pi/3
#       for values of t between 0 and 4pi

import numpy as np
import matplotlib.pyplot as plt

def customSin(A, f, theta0, t):
    y=A*np.sin(np.pi*2*f*t + theta0)
    return y

plt.close('all')

t0=0
t1=4*np.pi
fs=10
t=np.arange(t0, t1, 1/fs)

x1=customSin(1, 0.2, 0, t)
x2=customSin(1, 0.2, 2*np.pi/3, t)
x3=customSin(1, 0.2, -2*np.pi/3, t)

plt.figure()
plt.plot(t, x1, 'r')
plt.plot(t, x2, 'g')
plt.plot(t, x3, 'b')