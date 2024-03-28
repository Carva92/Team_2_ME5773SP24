# Authors: Julian Carvajal Rico
#          James Platt Standard
#          Roberto Enriquez Vargas

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

def save_results(results, filename):
    with open(filename, 'w') as file:
        # Write the header
        file.write("Quadrature no., Integral Value, Percent Error (%), Run Time (s)\n")
        # Write the data
        for result in results:
            file.write(f"{result['n']}, {result['Integral Value']}, {result['Percent Error']}%, {result['Run Time']}s\n")




# Additional function to handle distributing the work
def distribute_work(comm, size, num_integrations):
    for i in range(1, num_integrations + 1):
        worker = (i % (size - 1)) + 1
        comm.send(i, dest=worker, tag=1)
    # Sending a stop signal to all workers
    for i in range(1, size):
        comm.send(None, dest=i, tag=1)

# Function to handle worker tasks
def worker_task(comm, rank):
    while True:
        n = comm.recv(source=0, tag=1)
        if n is None:
            break
        start_time = time.time()
        integral = compute_integral(n)
        run_time = time.time() - start_time
        comm.send((integral, n, run_time), dest=0, tag=2)  # Send run time as well

# Function to collect results from workers
def collect_results(comm, num_integrations):
    results = []
    for _ in range(num_integrations):
        integral, n, run_time = comm.recv(source=MPI.ANY_SOURCE, tag=2)
        results.append({'n': n, 'Integral Value': integral, 'Run Time': run_time})
    return results



# Start the MPI process
comm = MPI.COMM_WORLD

# Determine total number of tasks
size = comm.Get_size()

# Determine id of "this" task
rank = comm.Get_rank()


exact_value = 2 / math.exp(1)


num_integrations = 20  # Total number of integrations to perform

# --- Master ---
if rank == 0:
    # Distribute work to the workers
    distribute_work(comm, size, num_integrations)
    
    # Collect the results
    results = collect_results(comm, num_integrations)


    # Compute percent error
    for result in results:
        integral = result['Integral Value']
        n = result['n']
        run_time = result['Run Time']
        percent_error = abs((integral - exact_value) / exact_value) * 100
        result['Percent Error'] = percent_error
        result['Run Time'] = run_time  # This is where you add the run time to the dictionary
        print(f"Master Received Integral Value {integral} From Process {n} Percent Error {percent_error:.2f}% And Run Time {run_time:.4f}s")

        
    # Sort the results
    results.sort(key=lambda x: x['n'])

    # Save results to a text file
    save_results(results, 'part2.txt')

# --- Worker ---
else:
    worker_task(comm, rank)




