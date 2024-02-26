# Homework 5


# Import Libraries
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



#start time for time to save A to csv
start_time_A_CSV = time.time()

#save file A.CSV
np.savetxt('A.CSV',A, fmt='%d', delimiter=',')

# evaluate calculation time for A
A_time_CSV = time.time() - start_time_A_CSV

print("The time to create A.CSV is : ", end="")
print('%.6f' % A_time_CSV)

#start time for time to save B to CSV
start_time_B_CSV = time.time()

#save file B.CSV
np.savetxt('B.CSV',B, fmt='%d', delimiter=',')

# evaluate calculation time for B
B_time_CSV = time.time() - start_time_B_CSV

print("The time to create B.CSV is : ", end="")
print('%.6f' % B_time_CSV)

#start time for time to save C to CSV
start_time_C_CSV = time.time()

#save file C.CSV
np.savetxt('C.CSV',C, fmt='%.18e', delimiter=',')

# evaluate calculation time for C
C_time_CSV = time.time() - start_time_C_CSV

print("The time to create C.CSV is : ", end="")
print('%.6f' % C_time_CSV)

#start time for time to save D to CSV
start_time_D_CSV = time.time()

#save file D.CSV
np.savetxt('D.CSV',D, fmt='%d', delimiter=',')

# evaluate calculation time for D
D_time_CSV = time.time() - start_time_D_CSV

print("The time to create D.CSV is : ", end="")
print('%.6f' % D_time_CSV)

#start time for time to save E to CSV
start_time_E_CSV = time.time()

#save file E.CSV
np.savetxt('E.CSV',E, fmt='%.7e', delimiter=',')

# evaluate calculation time for E
E_time_CSV = time.time() - start_time_E_CSV

print("The time to create E.CSV is : ", end="")
print('%.6f' % E_time_CSV)

print()

#start time for time to save A to .npy
start_time_A_npy = time.time()

#save file A.npy
np.save('A.npy',A)

# evaluate calculation time for A
A_time_npy = time.time() - start_time_A_npy

print("The time to create A.npy is : ", end="")
print('%.6f' % A_time_npy)

#start time for time to save B to .npy
start_time_B_npy = time.time()

#save file B.npy
np.save('B.npy',B)

# evaluate calculation time for B
B_time_npy = time.time() - start_time_B_npy

print("The time to create B.npy is : ", end="")
print('%.6f' % B_time_npy)

#start time for time to save C to .npy
start_time_C_npy = time.time()

#save file C.npy
np.save('C.npy',C)

# evaluate calculation time for C
C_time_npy = time.time() - start_time_C_npy

print("The time to create C.npy is : ", end="")
print('%.6f' % C_time_npy)

#start time for time to save D to .npy
start_time_D_npy = time.time()

#save file D.npy
np.save('D.npy',D)

# evaluate calculation time for D
D_time_npy = time.time() - start_time_D_npy

print("The time to create D.npy is : ", end="")
print('%.6f' % D_time_npy)

#start time for time to save E to .npy
start_time_E_npy = time.time()

#save file E.npy
np.save('E.npy',E)

# evaluate calculation time for E
E_time_npy = time.time() - start_time_E_npy

print("The time to create E.npy is : ", end="")
print('%.6f' % E_time_npy)
print()











