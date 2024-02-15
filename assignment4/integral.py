# Import necessary libraries
import math
import time
import numexpr
import numpy as np

# Define N and deltax
N = 10**9
deltax = 2/N

#starting section 3.2

#  start time for F1 time
start_time = time.time()

#creating varible F1 with value of zero
F1 = 0.0

#for loop through all 1 billion values
for i in range(N):
    
    #calculate value Xi

    Xi = ((deltax * i) - 1)
    FXi = math.sqrt(4 - (4 * (Xi**2)))
    F1 = F1 + (FXi * deltax)

# end for

# evaluate calculation time for F1
F1_time = time.time() - start_time

print("The time to compute F1 using a for loop is : ", end="") 
print('%.6f' % F1_time) 

print("F1 value calculated using a for loop : ", end="") 
print('%.16f' % F1)
print()

# Using numpy's vectorized functions
start_time = time.time()
i_vec = np.arange(N)
x_vec = (2 * i_vec / N) - 1
F_vec = np.sqrt(4 - 4 * x_vec**2)
F2 = np.sum(F_vec) * deltax
elapsed_time_numpy = time.time() - start_time
print(f"The time to compute F2 using numpy vectorized functions is : {elapsed_time_numpy:.6f}")
print(f"F2 value calculated using numpy vectorized functions : {F2:.16f}")
print()
# Using numexpr evaluations
start_time = time.time()
i_vec = np.arange(N)
x_vec = numexpr.evaluate('(2 * i_vec / N) - 1')
F_vec = numexpr.evaluate('sqrt(4 - 4 * x_vec**2)')
F3 = numexpr.evaluate('sum(F_vec)') * deltax
elapsed_time_numexpr = time.time() - start_time
print(f"The time to compute F3 using numexpr evaluations is : {elapsed_time_numexpr:.6f}")
print(f"F3 value calculated using numexpr evaluations : {F3:.16f}")
print()
