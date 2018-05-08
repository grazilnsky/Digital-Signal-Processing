# -*- coding: utf-8 -*-

#2.39 - solve the system
#       x+y+z=3
#       x-y-z=-1
#       x-3x+2y=0


import numpy as np

coeffs=np.array([[1, 1, 1],
                 [1, -1, -1], 
                 [-2, 2, 0]])

#compute the determinant of the matrix of coefficients
d=np.linalg.det(coeffs)

freeTerms = np.array([[3],
                      [-1],
                      [0]])

#compute x using Cramer's rule
Ax = np.array([[3,1,1],
              [-1,-1,-1],
              [0,2,0]])
dx=np.linalg.det(Ax)
x=dx/d

#compute y using Cramer's rule
Ay = np.array([[1,3,1],
               [1,-1,-1], 
               [-2,0,0]])
dy=np.linalg.det(Ay)
y=dy/d

#compute z using Cramer's rule
Az = np.array([[1,1,3],
               [1,-1,-1],
               [-2,2,0]])
dz=np.linalg.det(Az)
z=dz/d

solutions=np.array([x,y,z])
print(solutions)