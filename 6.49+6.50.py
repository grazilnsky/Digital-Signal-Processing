# -*- coding: utf-8 -*-

#6.49 - Create a FIR filter. The filter parameters are the cutting frequencies and the width of the transfer band. 
#       Use the filter to filter the wave, display the output function of time, display the fft of the output,
#       and play the sound before and after filtering.
#   HP filter
#6.50 - Create a function that will implement the window method for filter design.
#   Rectangular method

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf
import scipy.signal as dsp
   
def rectangular(M):
    t=np.arange(0,M,1)
    rec=[]
    for x in t:
        rec.append(1)
    return rec

plt.close('all')

x,fs=sf.read('DSP.wav')
sd.play(x,fs)
sd.wait()
plt.figure('Original Signal')
plt.plot(x, color='orange')

cutoff = 2000.0    # Desired cutoff frequency, Hz
trans_width = 250  # Width of transition from pass band to stop band, Hz
numtaps = 125      # Size of the FIR filter.

b = dsp.remez(numtaps, [0, cutoff - trans_width, cutoff, 0.5*fs], [0, 1], Hz=fs)
w, h = dsp.freqz(b, [1], worN=2000)

#frequency response of the filter in db
plt.figure('Frequency Response')
plt.plot(0.5*fs*w/np.pi, 20*np.log10(np.abs(h)))
plt.grid(True)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')

#plot and play the filtered signal
xFIR = dsp.filtfilt(b, [1], x, axis=0)
plt.figure('Filtered Signal')
plt.plot(xFIR, color='orange')
sd.play(xFIR, fs)
sd.wait()

#fft of the output
xFFT=np.fft.fft(xFIR)
plt.figure('FFT of Filtered Signal')
plt.plot(abs(xFFT))

#6.50 rectangular window
plt.figure('Rectangular window')
plt.plot(np.arange(0,50, 1), rectangular(50))