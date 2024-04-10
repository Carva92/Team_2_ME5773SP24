import numpy as np
import module as md

def main():
    A = np.random.rand(100, 100).astype(np.float64)
    B = np.random.rand(100, 100).astype(np.float64)
    C = md.matmul_cython(A, B)
    print("Matrix multiplication result:")
    print(C)

if __name__ == "__main__":
    main()
