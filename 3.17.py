# -*- coding: utf-8 -*-

#3.17 - Generate a sequence of 1000 random numbers in the interval [-1, 1]. Plot it.
#       Plot the histogram of the data.

import random
import numpy as np
import matplotlib.pyplot as plt


plt.close('all')


r=[]
for i in range(1000):
    r.append(round(random.uniform(-1, 1), 1))   #generate the sequence of numbers with 1 decimal each

t=np.arange(0,1000, 1)



plt.figure()
plt.scatter(t, r)
plt.plot(t, r, 'r')
plt.grid()

plt.figure()
plt.hist(r, histtype='step')
plt.grid()
plt.show()
