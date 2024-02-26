# Import libraries time, numpy, and h5py
import time
import numpy as np
import h5py

# Loading CSV Matrix files: A,B, C,D,&E
st_csv_A = time.time()
A_csv = np.loadtxt("A.csv", delimiter=',', dtype='int64')    # 64-bit integer
et_csv_A = time.time()
B_csv = np.loadtxt("B.csv", delimiter=',', dtype='int8')     # 8-bit integer
et_csv_B = time.time()
C_csv = np.loadtxt("C.csv", delimiter=',', dtype='float64')  # 8-byte float
et_csv_C = time.time()
D_csv = np.loadtxt("D.csv", delimiter=',', dtype='int16')    # 2-byte integer
et_csv_D = time.time()
E_csv = np.loadtxt("E.csv", delimiter=',', dtype='float32')  # 4-byte float
et_csv_E = time.time()
print(f"Time to load all csv files: {et_csv_E-st_csv_A} seconds")
print(f"\tTime to load A.csv file: {et_csv_A-st_csv_A}")
print(f"\tTime to load B.csv file: {et_csv_B-et_csv_A}")
print(f"\tTime to load C.csv file: {et_csv_C-et_csv_B}")
print(f"\tTime to load D.csv file: {et_csv_D-et_csv_C}")
print(f"\tTime to load E.csv file: {et_csv_E-et_csv_D}")

# Loading  npy Matrix files: A,B,C,D,&E
st_npy_A = time.time()
A_npy = np.load('A.npy')
et_npy_A = time.time()
B_npy = np.load('B.npy')
et_npy_B = time.time()
C_npy = np.load('C.npy')
et_npy_C = time.time()
D_npy = np.load('D.npy')
et_npy_D = time.time()
E_npy = np.load('E.npy')
et_npy_E = time.time()
print(f"Time to load all npy files: {et_npy_E-st_npy_A} seconds")
print(f"\tTime to load A.npy file: {et_npy_A-st_npy_A} seconds")
print(f"\tTime to load B.npy file: {et_npy_B-et_npy_A} seconds")
print(f"\tTime to load C.npy file: {et_npy_C-et_npy_B} seconds")
print(f"\tTime to load D.npy file: {et_npy_D-et_npy_C} seconds")
print(f"\tTime to load E.npy file: {et_npy_E-et_npy_D} seconds")


# Loading h5py files: A,B,C,D,&E
f = h5py.File('matrix_db.hdf5',"r+")
ds_A = f['integer_group/A']
ds_B = f['integer_group/B']
ds_C = f['float_group/C']
ds_D = f['integer_group/D']
ds_E = f['float_group/E']

ts_A = time.time()                 
A_mat = ds_A[...]          # Loading A matrix
te_A = time.time()

ts_B = time.time()
B_mat = ds_B[...]           # Loading B matrix
te_B = time.time()

ts_C = time.time()
C_mat = ds_C[...]           # Loading C matrix
te_C = time.time()

ts_D = time.time()
D_mat = ds_D[...]           # Laoding D matrix
te_D = time.time()

ts_E = time.time()
E_mat = ds_E[...]           # Loading E matrix
te_E = time.time()

print(f"Time to open h5py databases: {te_E-ts_A} seconds")
print(f"\tTime to open A matrix from h5py file: {te_A-ts_A} seconds")
print(f"\tTime to open B matrix from h5py file: {te_B-ts_B} seconds")
print(f"\tTime to open C matrix from h5py file: {te_C-ts_C} seconds")
print(f"\tTime to open D matrix from h5py file: {te_D-ts_D} seconds")
print(f"\tTime to open E matrix from h5py file: {te_E-ts_E} seconds")
