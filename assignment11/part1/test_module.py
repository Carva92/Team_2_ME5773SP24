import numpy as np
import searchUtilsTeam02 as search


sorted_array = np.array([0.1, 0.3, 0.5, 0.7, 0.9, 1.2, 1.4, 1.6, 1.8, 2.0], dtype=np.float64)
unsorted_array = np.array([1.8, 2.0, 0.1, 0.3, 1.6, 1.4, 0.5, 0.7, 0.9, 1.2], dtype=np.float64)


x = 2.0


idx = search.searchutils.linearsearch(sorted_array,x)
print("index computed with linear search:", idx)

idx = search.searchutils.binarysearch(sorted_array,x)
print("index computed with binary search:", idx)

idx = search.searchutils.linearsearch(unsorted_array,x)
print("index computed with linear search and unsorted array:",idx)



