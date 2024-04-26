import numpy as np
import searchUtilsTeam02 as search
import time

# number of elements
num_elements = 10**7

# array with unique elements
array = np.linspace(-10, 10, num_elements, endpoint=False)
np.random.shuffle(array)

#sort for searches that require a sorted array
sorted_array = np.sort(array)

#fortran linear search
start_time = time.time()

idx = search.searchutils.linearsearch(array,array[-2])
print("index computed with linear search:", idx)

fortran_time_linear = time.time() - start_time
print(f"The time to find X[-2]  using fortran linear search is : {fortran_time_linear:.6f}")

print()

#fortran binary search
start_time = time.time()


idx = search.searchutils.binarysearch(sorted_array,sorted_array[-2])
print("index computed with binary search:", idx)

fortran_time_binary = time.time() - start_time
print(f"The time to find X[-2] using fortran binary search is : {fortran_time_binary:.6f}")

print()

#numpy search sorted
start_time = time.time()

#sorted_array = np.sort(array)

idx = np.searchsorted(sorted_array,sorted_array[-2])
print("index computed with numpy sorted search:", idx)

numpy_time_sorted = time.time() - start_time
print(f"The time to find X[-2] using numpy sorted search is : {numpy_time_sorted:.6f}")

print()

#numpy search
start_time = time.time()

idx = np.where(array == array[-2])
print("index computed with numpy search:", idx)

numpy_time_search = time.time() - start_time
print(f"The time to find X[-2] using numpy search is : {numpy_time_search:.6f}")


print()


