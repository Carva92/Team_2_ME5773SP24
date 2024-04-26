# Import Libraries
import numpy as np
import time

# Initialize N
N = 10000
print(f"N: {N}")

# Start timing for the creation of K and f
start_time = time.time()

# Create the matrix K full of Zeros
K = np.zeros((N, N))

# Populate the K matrix with the corresponding numbers
for i in range(N):
    K[i, i] = 2
    if i > 0:
        K[i, i-1] = -1
        K[i-1, i] = -1
# Set the last element K_NN with 1
K[N-1, N-1] = 1  

# Create the vector f
f = np.zeros(N)
f[N-1] = 1/N

# Measure and print the time elapsed for creating K and f
creation_time = time.time() - start_time
print(f"Time elapsed to create K and f: {creation_time:.9f} sec")

# Solve the system of equations Ku=f
start_time = time.time()
u = np.linalg.solve(K, f)


# Measure and print the time elapsed for solving the system
solution_time = time.time() - start_time
print(f"Time elapsed to solve the system: {solution_time:.9f} sec")

# Print the last item of the solution vector u
print(f"The last item of the vector u: {int(u[-1])}")
