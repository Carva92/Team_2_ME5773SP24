# Authors: Julian Carvajal Rico
#          James Platt Standard
#          Roberto Enriquez Vargas

# In this firts code we assigned exacly 21 tasks to cover 1 master and 20 workers, in which each task is assigned to each worker.

from mpi4py import MPI
import time
import numpy as np
import math
import sys


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



def compute_integral(n):
    x = np.zeros(n)
    w = np.zeros(n)
    gauleg(-1, 1, x, w, n)
    return np.sum(w * f(x))


# Function to save the outputs into the desire file            
def save_results(results, filename):
    with open(filename, 'w') as file:
        # Write the header
        file.write("Quadrature no., Integral Value, Percent Error (%), Run Time (s)\n")
        # Write the data
        for result in results:
            file.write(f"{result['n']}, {result['Integral Value']}, {result['Percent Error']}%, {result['Run Time']}s\n")



# Start the MPI process
comm = MPI.COMM_WORLD

# Determine total number of tasks
size = comm.Get_size()

# Determine id of "this" task
rank = comm.Get_rank()


exact_value = 2 / math.exp(1)


# --- Master ---
if rank == 0:
    results = []

    for i in range(1, size):
        # Time the sending and receiving of data
        start_time = time.time()

        # Send quadrature to worker i
        comm.send(i, dest=i, tag=1)

        # Receive results from worker i
        integral = comm.recv(source=i, tag=2)
        end_time = time.time()

        # Compute run time
        run_time = end_time - start_time
        # Compute percent error
        percent_error = abs((integral - exact_value) / exact_value) * 100
        print(f"Master Received Integral Value {integral} From Process {i} Percent Error {percent_error} And Run Time {run_time}")
        results.append({'n': i, 'Integral Value': integral, 'Percent Error': percent_error, 'Run Time': run_time})

    # Save results to a text file
    save_results(results, 'part1.txt')

# --- Worker ---
else:
    # Wait to receive n from master
    n = comm.recv(source=0, tag=1)

    # Compute integral
    integral = compute_integral(n)

    # Send integral back to master
    comm.send(integral, dest=0, tag=2)





