# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 00:11:30 2024

@author: hp
"""

import numpy as np
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix[0,:])#gives first row
print(matrix[:,2])#gives last column
print(matrix[1:3,1:3])#gives 2x2 matrix of center