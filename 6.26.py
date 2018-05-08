# -*- coding: utf-8 -*-

#6.26 - Design a digital Butterworth filter of order 30 
#       with a cutoff frequency of 100 Hz, working at a
#       sample rate of 500 Hz. Represent graphically and
#       compare with the result from example 6.13

import numpy as np
from scipy.signal import butter, freqz
import matplotlib.pyplot as plt


def butter_lowpass(cutoff, fs, order):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

plt.close("all")
# filter requirements.
order = 30
fs = 500      # sample rate
cutoff = 100  # cutoff frequency of the filter

#filter coefficients for checking the filter's frequency response.
b, a = butter_lowpass(cutoff, fs, order)
w, h = freqz(b, a)

# plot the frequency response.
plt.figure()
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
plt.axvline(cutoff, color='k')
plt.xlim(0, 0.5*fs)
plt.title("Frequency Response")
plt.xlabel('Frequency [Hz]')
plt.grid()
plt.show()


