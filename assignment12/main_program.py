import cupy as cp
import time as time
import numpy as np


defK_kernel = cp.RawKernel(r'''
extern "C" __global__
void defK(double* K, int ncols, int nrows) {

    /*
     This function defines a square matrix K (row-major format)
     with all elements in the diagonal as 4 and all elements 
     next to the diagonal as -2. The last element of the diagonal
     set to 2. All other elements are set to zero.
     INPUTS: 
     - K: Pointer to the memory in K.
     - nrows: Number of rows of the matrix
     - ncols: Number of columns of the matrix
     */
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    int j = blockDim.y * blockIdx.y + threadIdx.y;
    
    if ((i < nrows) && (j < ncols)) {
        long long index = i * ncols + j;
        if (i == j) {
            K[index] = (i == nrows - 1) ? 2.0 : 4.0;
        } else if (abs(i - j) == 1) {
            K[index] = -2.0;
        } else {
            K[index] = 0.0;
        }
    }
}
''', 'defK')


block_dim = 16

# Test Code

# N = 10
# K = cp.empty((N, N), dtype=cp.float64)
# f = cp.array([1] * N, dtype=cp.float64)

# grid_dim = (N + block_dim - 1) // block_dim

# t_start = time.time()
    
# defK_kernel((grid_dim, grid_dim, 1), (block_dim, block_dim, 1), (K, N, N))

# # Solve the system using cupy
# u = cp.linalg.solve(K, f)

# t_end = time.time()

# print(u)
# print(f"Time spent creating the matrix and solving: {t_end - t_start:.6f} s")


# Large Matrix System

N_large = 30000
grid_dim_large = (N_large + block_dim - 1) // block_dim
K_large = cp.empty((N_large, N_large), dtype=cp.float64)
f_large = cp.zeros(N_large, dtype=cp.float64)
f_large[-1] = 1.0 / N_large

t_start_large = time.time()

defK_kernel((grid_dim_large, grid_dim_large, 1), (block_dim, block_dim, 1), (K_large, N_large, N_large))
u_large = cp.linalg.solve(K_large, f_large)

t_end_large = time.time()
print('K Matrix: ', K_large)
print('Vector f: ', f_large)
print(f"Time spent creating the matrix and solving using Cupy: {t_end_large - t_start_large:.6f} s")
print('Solution u: ', u_large)


# NumPy Version

t_start_np = time.time()

K_np = np.zeros((N_large, N_large), dtype=np.float64)
np.fill_diagonal(K_np, 4)
np.fill_diagonal(K_np[1:], -2)
np.fill_diagonal(K_np[:,1:], -2)
K_np[-1, -1] = 2
f_np = np.zeros((N_large,1), dtype=np.float64)
f_np[-1,0] = 1.0 / N_large
u_np = np.linalg.solve(K_np, f_np)

t_end_np = time.time()


print('K Matrix: ', K_np)
print('Vector f: ', f_np)
print(f"Time spent creating the matrix and solving using Numpy: {t_end_np - t_start_np:.6f} s")
print('Solution u: ', u_np)


