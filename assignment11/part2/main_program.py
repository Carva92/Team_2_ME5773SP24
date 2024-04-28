import module as md
import numpy as np
import time



# Initialize dense matrix 
N = 10000

# Creating Matrix A of size N x N (K in assignment 4)
A = np.zeros((N, N))
for i in range(N):
    A[i, i] = 2
    if i > 0:
        A[i, i - 1] = -1
        A[i - 1, i] = -1
A[N - 1, N - 1] = 1  # Adjust the last diagonal element

A_lower = np.tril(A)

# Creating vector b (f in assignment 4)
b = np.zeros(N)
b[N - 1] = 1 / N
b = b.reshape(N, 1)



print('Coefficient Matrix A:')

print(A)

print('Right-hand Side Matrix B:')

print(b)


t_start = time.time()
res = md.mkl_solver( A,b )
t_end = time.time()

#print('The Factor of A is:')

#print(A)

print('The Solution b of the system is: ')

print(b)


print('Time spent Unsymmetric: {0:.6f} s'.format(t_end-t_start))

b = np.zeros(N)
b[N - 1] = 1 / N
b = b.reshape(N, 1)

t_start = time.time()
res = md.mkl_solver_symm( A_lower,b )
t_end = time.time()

#print('The Factor of A is:')

#print(A)

print('The Solution b of the system is: ')

print(b)


print('Time spent Symmetric: {0:.6f} s'.format(t_end-t_start))


