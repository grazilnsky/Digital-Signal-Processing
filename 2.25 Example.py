# -*- coding: utf-8 -*-

#2.25 - the diag function in matlab will extract the main diagonal from the matrix B

import numpy as np

B=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(B)
print("The diagonal of B is: ", np.diag(B))