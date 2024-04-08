import numpy as np
import time
import os
from numba import jit, prange


@jit(nopython=True)
def myfunct(x):
    """
    Defines the function to be integrated.

    INPUTS:
    - x: double, evaluation point.

    OUTPUTS:
    - double, evaluated function.
    
    """

    return np.sin(x*x)+x/2

# end function


@jit(nopython=True, parallel=True)
def integral_riemann(a,b,N):
    """
    Implements the Riemann integration for the function
    myfunct(x).

    INPUTS:
    - a: double, Lower integration limit.
    - b: double, Upper integration limit.
    - N: Int, Number of integration regions.

    OUTPUTS:
    - double, evaluated integral.
    
    """
    dx = (b-a)/N
    F = 0
    
    for i in prange(N):
        x = a + i*dx
        F += myfunct(x)*dx
    # end for 

    return F

# end function

if __name__ == '__main__':

    # If needed, add dummy call to the integral_riemann
    # function here

    a = 0
    b = 2
    N = 100_000_000 # 10**8 
    F = integral_riemann(a,b,N)
    t_end = time.time()

    serial_time = None
    results = []

    # Evaluate the CPU time and integration here.

    for num_threads in [1, 2, 4, 8, 16, 20]:
        os.environ['NUMBA_NUM_THREADS'] = str(num_threads)

        # Dummy call to ensure JIT compilation
        integral_riemann(a, b, 1000)

        t_start = time.time()
        F = integral_riemann(a, b, N)
        t_end = time.time()

        cpu_time = t_end - t_start

        if num_threads == 1:
            serial_time = cpu_time

        speedup = serial_time / cpu_time
        efficiency = speedup / num_threads

        results.append((num_threads, cpu_time, speedup, efficiency))
        print(f'Threads: {num_threads}, CPU time: {cpu_time:.6f}s, Speedup: {speedup:.2f}, Efficiency: {efficiency:.2f}')
        print('Integral {0:f}'.format(F))

# end if
