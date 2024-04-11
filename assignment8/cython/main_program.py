import numpy as np
import module as md
import time







def main():
    sizes = [3, 10, 100, 1000]
    

    
    for size in sizes:
    
        #start_time = time.time()
        A = np.random.rand(size, size).astype(np.float64)
        B = np.random.rand(size, size).astype(np.float64)
        
        #cython implementation
        start_time_C = time.time()
        C = md.matmul_cython(A, B)
        end_time_C = time.time()-start_time_C
        
        print("Matrix multiplication result:")
        #print(C)
        print("time to run",size,"by", size, "using Cython is",end_time_C)
            
        #numpy implementation
        start_time_N = time.time()
        Numpy_C = np.dot(A, B)
        end_time_N = time.time()-start_time_N

        print("time to run", size,"by", size, "using Numpy is", end_time_N)


if __name__ == "__main__":
    main()

