import module as md
import numpy as np
import time




A =  np.array([[    -5.86,    3.99,    -5.93,     -2.82,    7.69, ],
               [     3.99,    4.46,     2.58,      4.42,    4.61, ],
               [    -5.93,    2.58,    -8.52,      8.57,    7.69, ],
               [    -2.82,    4.42,     8.57,      3.72,    8.07, ],
               [     7.69,    4.61,     7.69,      8.07,    9.83, ]])

A_lower = np.tril(A)

b = np.array([[    1.32,  -6.33,  -8.77, ],
              [    2.22,   1.69,  -8.33, ],
              [    0.12,  -1.56,   9.54, ],
              [   -6.41,  -9.49,   9.56, ],
              [    6.33,  -3.67,   7.48, ]])





print('Coefficient Matrix A:')

print(A)

print('Right-hand Side Matrix B:')

print(b)


t_start = time.time()
res = md.mkl_solver( A,b )
t_end = time.time()

print('The Factor of A is:')

print(A)

print('The Solution b of the system is: ')

print(b)


print('Time spent Unsymmetric: {0:.6f} s'.format(t_end-t_start))

b = np.array([[    1.32,  -6.33,  -8.77, ],
              [    2.22,   1.69,  -8.33, ],
              [    0.12,  -1.56,   9.54, ],
              [   -6.41,  -9.49,   9.56, ],
              [    6.33,  -3.67,   7.48, ]])

t_start = time.time()
res = md.mkl_solver_symm( A_lower,b )
t_end = time.time()

print('The Factor of A is:')

print(A)

print('The Solution b of the system is: ')

print(b)


print('Time spent Symmetric: {0:.6f} s'.format(t_end-t_start))


