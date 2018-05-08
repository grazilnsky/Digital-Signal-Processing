# -*- coding: utf-8 -*-

#3.56 - Write a function sampleAndHoldD that will receive a string
#       representing a function, the starting time t0, the end time t1 and 
#       the sampling frequency fs. This function will return the sampling vector
#       and the values of the specified function for the instants.

import myCode as mc
import numpy as np
import matplotlib.pyplot as plt

def sampleAndHoldD(func,t0,t1,fs):
    t=np.arange(t0,t1,1/fs)
    if func=="sawtooth":
        y=mc.mySawtooth(1,1, t)
        return y
    if func=="square":
        y=mc.mySquare(1,1,t)
        return y
    if func=="triangle":
        y=mc.myTriangle(1,1,t)
        return y
    if func=="chirp":
        y=mc.myExponentialChirp(1,1,1,5,t)
        return y
    
plt.close("all")

plt.figure()
plt.plot(sampleAndHoldD("sawtooth", -8*np.pi, 8*np.pi, 100))
plt.figure()
plt.plot(sampleAndHoldD("square", -8*np.pi, 8*np.pi, 100))
plt.figure()
plt.plot(sampleAndHoldD("triangle", -8*np.pi, 8*np.pi, 100))
plt.figure()
plt.plot(sampleAndHoldD("chirp", -8*np.pi, 8*np.pi, 100))