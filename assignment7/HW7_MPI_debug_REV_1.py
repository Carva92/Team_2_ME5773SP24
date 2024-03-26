from mpi4py import MPI
import time
import numpy as np
import math


def f(x):
    return x*np.exp(x)



def gauleg(x1, x2, x, w, n):
    EPS = 3.0e-16
    m = (n + 1) // 2
    xm = 0.50 * (x2 + x1)
    xl = 0.50 * (x2 - x1)
    
    for i in range(1, m + 1):
        z = math.cos(math.pi * (i - 0.25) / (n + 0.50))
        while True:
            p1 = 1.0
            p2 = 0.0
            for j in range(1, n + 1):
                p3 = p2
                p2 = p1
                p1 = ((2.0 * j - 1.0) * z * p2 - (j - 1.0) * p3) / j
            
            pp = n * (z * p1 - p2) / (z * z - 1.0)
            z1 = z
            z = z1 - p1 / pp
            
            if abs(z - z1) > EPS:
                continue
            
            x[i - 1] = xm - xl * z
            x[n - i] = xm + xl * z
            w[i - 1] = 2.0 * xl / ((1.0 - z * z) * pp * pp)
            w[n - i] = w[i - 1]
            break

# Start the MPI process
comm = MPI.COMM_WORLD

# Determine total number of tasks
size = comm.Get_size()

# Determine id of "this" task
rank = comm.Get_rank()


# --- Master ---
if rank == 0:
        
        #empty list to store results
        integral_results = []


    # Loop to send quadrature to workers
        for n in range(1, size):
              # Compute quadrature values
             
             x = np.zeros(n)
             w = np.zeros(n)
             gauleg(-1, 1, x, w, n)


             quadrature = (x, w) 
             
            # print("quadrature is equal to : ",quadrature)

             comm.send(quadrature, dest=n)    

        # Receive and collect results from worker processes
        for i in range(1, size):
            integral = comm.recv(source=i)  # receive result from worker i
            integral_results.append(integral) # accumulate integral
            print(f"Master received value {integral} from process {i}")  # report who sent results
        
        print("integral results for 1 through n",integral_results)
        
        exact = 2/math.exp(1)
       # print("exact is equal to :",exact)
        IR = np.array(integral_results)
        relative_error = (abs((IR-exact)/exact))
        print("relative error : ",relative_error)



# --- Worker ---
else:
    # Print notification including process id
    print(f"Process {rank} starts")

     # Receive quadrature from master
    quadrature = comm.recv(source=0)
    
    x, w = quadrature  #split up quadrature
    


    #calculate integral
    integral = np.sum(w * f(x))
    
    

    # Send results back to Master (rank = 0)
    comm.send(integral, dest=0)














