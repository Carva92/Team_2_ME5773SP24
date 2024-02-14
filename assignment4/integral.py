# Import necessary libraries
import math
import time
import numexpr
import numpy as np

# Define N and deltax
N = 10**9
deltax = 2/N

# Using a for loop
start_time = time.time()
F1 = 0.0
for i in range(N):
    x_i = (2 * i / N) - 1
    f_xi = math.sqrt(4 - 4 * x_i**2)
    F1 += f_xi * deltax
elapsed_time_for_loop = time.time() - start_time
print(f"{elapsed_time_for_loop:.6f}")
print(f"{F1:.16f}")

# Using numpy's vectorized functions
start_time = time.time()
i_vec = np.arange(N)
x_vec = (2 * i_vec / N) - 1
F_vec = np.sqrt(4 - 4 * x_vec**2)
F2 = np.sum(F_vec) * deltax
elapsed_time_numpy = time.time() - start_time
print(f"{elapsed_time_numpy:.6f}")
print(f"{F2:.16f}")

# Using numexpr evaluations
start_time = time.time()
i_vec = np.arange(N)
x_vec = numexpr.evaluate('(2 * i_vec / N) - 1')
F_vec = numexpr.evaluate('sqrt(4 - 4 * x_vec**2)')
F3 = numexpr.evaluate('sum(F_vec)') * deltax
elapsed_time_numexpr = time.time() - start_time
print(f"{elapsed_time_numexpr:.6f}")
print(f"{F3:.16f}")
