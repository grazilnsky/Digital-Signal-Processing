# -*- coding: utf-8 -*-

#2.33 - write a function to plot the solutions of 
#       the equation z^n-a=0, with n,a in N

import matplotlib.pyplot as plt
import sympy.solvers as sv
from sympy import Symbol

def solveEq(n,a):  
    x=Symbol('x')
    s=sv.solve(x**n-a,x)  #solve the equation for x
    plt.figure()
    for x in s:
        x=(complex)(x)   #convert from object to complex number
        plt.scatter(x.real, x.imag)


solveEq(847, 91300)   


    

