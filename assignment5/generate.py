import time
import numpy as np
import h5py



#start of code

#nxn size of A

size_A = 5000

#nxn matrix between the values of 2 and 9, 10 is one above the largest integer to be drawn

A = np.random.randint(2,10,(size_A,size_A),dtype=np.int64)

#print matrix to check 
#print(np.matrix(A))

size_B = 5000

#nxn matrix between the values of 100 and 127, 128 is one above the largest integer to be drawn

B = np.random.randint(100,128,(size_B,size_B),dtype=np.int8)

#print matrix to check
#print(np.matrix(B))

#nxn size of C

size_C = 5000

#nxn matrix with 0.33333 in all values

C = np.full((size_C,size_C),0.33333,dtype=np.float64,order='C')

#print matrix to check
#print(np.matrix(C))

#nxn matrix with values between 1001 and 1100 in Fortran order

D = np.arange(1001,1101,dtype=np.int16).reshape((10,10), order='F')

#print matrix to check
#print(np.matrix(D))

#nxn matrix with values between 350.0 and 350.3 in C order

E = np.arange(350.0,350.4,0.1,dtype=np.float32).reshape((2,2), order='C')

#print matrix to check
#print(np.matrix(E))










