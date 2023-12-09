#Marco Vivian 09/12/2023


print("First script")

import pandas as pd
import numpy as np

#array as numbers
x = np.array([1,2,3,4,5])
print(x)
print(x[0])
#multidimensional array as list of list
y = np.array([[1,2],[3,4],[5,6]])
print(y)
print(y[0,1])

#shape ci ritorna le dimensioni
print(x.shape)
print(y.shape)

print(y.shape[0],y.shape[1])

print(len(y.shape))


print(y)
# usiamo numero elementi e esce una sola riga
print(y.reshape(6))

#-1 capisce da solo
print(y.reshape(-1))

#sistema array su 2 righe e 3 colonne
print(y.reshape(2,3))

#-1 capisce da solo il numero di colonne date le 2 righe definite
print(y.reshape(2,-1))

x2 = np.array([1,2,3,4,5,6])
print(x2)

print(x2.reshape(3,2))






















