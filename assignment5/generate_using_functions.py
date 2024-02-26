#Homework5


# Code By: Julian Carvajal Rico
#          James Platt Standard
#          Roberto Enriquez Vargas


import time
import numpy as np
import h5py


# Functions for the creation of the corresponding Matrix

def create_matrix_a():
    return np.random.randint(2, 10, size=(5000, 5000), dtype=np.int64)

def create_matrix_b():
    return np.random.randint(100, 128, size=(5000, 5000), dtype=np.int8)

def create_matrix_c():
    return np.full((5000, 5000), 0.33333, dtype=np.float64)

def create_matrix_d():
    shape = (10, 10)
    return np.linspace(1001, 1100, num=shape[0]*shape[1], dtype=np.int16).reshape(shape, order='F')

def create_matrix_e():
    shape = (2, 2)
    return np.linspace(350.0, 350.3, num=shape[0]*shape[1], dtype=np.float32).reshape(shape, order='C')

# Function to save each matrix into the corresponding format

def export_matrix(matrix, name, dtype):
    start_time = time.time()
    if dtype == 'int':
        np.savetxt(f"{name}.csv", matrix, fmt='%d', delimiter=',')
    elif dtype == 'float64':
        np.savetxt(f"{name}.csv", matrix, fmt='%.18e', delimiter=',')
    elif dtype == 'float32':
        np.savetxt(f"{name}.csv", matrix, fmt='%.7e', delimiter=',')
    print(f"Time to generate {name}.csv: {time.time() - start_time} seconds")

    start_time = time.time()
    np.save(f"{name}.npy", matrix)
    print(f"Time to generate {name}.npy: {time.time() - start_time} seconds")

# Create a variable calling each function to create each Matrix in the corresponding format

matrices = [
    ('A', create_matrix_a(), 'int'),
    ('B', create_matrix_b(), 'int'),
    ('C', create_matrix_c(), 'float64'),
    ('D', create_matrix_d(), 'int'),
    ('E', create_matrix_e(), 'float32'),
]

# Loop to save each Matrix

for name, matrix, dtype in matrices:
    export_matrix(matrix, name, dtype)





#start time for the entire operation of HDF5

start_time = time.time()  


# Create an HDF5 file
with h5py.File('matrix_db.hdf5', 'w') as hdf:

    # Create groups
    integer_group = hdf.create_group('integer_group')
    float_group = hdf.create_group('float_group')

    # Add attribute to integer_group
    integer_group.attrs['description'] = 'Matrices with integer values'

    # Add matrices to integer_group with the specified configurations
    # Matrix A
    start_time_a = time.time()  # Record start time for matrix A
    integer_group.create_dataset('A', data=matrices[0][1], chunks=(500, 500), compression='gzip')
    print(f"Time to create dataset A in HDF5 file: {time.time() - start_time_a} seconds")

    # Matrix B
    start_time_b = time.time()  # Record start time for matrix B
    integer_group.create_dataset('B', data=matrices[1][1], chunks=(1000, 1000), compression='gzip')
    print(f"Time to create dataset B in HDF5 file: {time.time() - start_time_b} seconds")

    # Matrix D
    start_time_d = time.time()  # Record start time for matrix D
    integer_group.create_dataset('D', data=matrices[3][1], compression='gzip')  # Default chunk size
    print(f"Time to create dataset D in HDF5 file: {time.time() - start_time_d} seconds")

    # Add matrices to float_group with the specified configurations
    # Matrix C
    start_time_c = time.time()  # Record start time for matrix C
    float_group.create_dataset('C', data=matrices[2][1], compression='gzip')  # Default chunk size
    print(f"Time to create dataset C in HDF5 file: {time.time() - start_time_c} seconds")

    # Matrix E
    start_time_e = time.time()  # Record start time for matrix E
    float_group.create_dataset('E', data=matrices[4][1])  # No compression for E
    print(f"Time to create dataset E in HDF5 file: {time.time() - start_time_e} seconds")

print(f"Total time to create HDF5 file: {time.time() - start_time} seconds")