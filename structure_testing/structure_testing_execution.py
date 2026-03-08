# test1.py is for small arrays
from implementation import *
import time
import numpy as np
import os
import inspect
import sys

mapping = {
    1 : insertion_sort,
    2 : merge_sort,
    3 : bubble_sort,
    4 : quicksort,
    5 : selection_sort,
    6 : non_optimized_timsort,
    7 : optimized_timsort
}
n_logn_algorithms = set([2,4,6,7])
num_of_algoritms = 7
num_of_tests = 5

def saving_result(algorithm_number,duration,test_number):
    with open('structure_testing_results.txt','a') as file:
        data = f"Algorithm {algorithm_number} took {duration:.20f} seconds for test {test_number}.\n"
        print(data)
        file.write(data)
        
    

for j in range(5,num_of_tests + 1):
    file_path = f"structure_testing/test{j}.npy"
    arrays = np.load(file_path,allow_pickle=True)
    for i in range(1,num_of_algoritms + 1):
        if i ==4:
            continue
        if j > 4 and i not in n_logn_algorithms:
            continue
        duration = 0
        algo = mapping[i]
        sig = inspect.signature(algo)
        num_args = len(sig.parameters)
        for array in arrays:
            test_array = list(np.copy(array))
            if num_args == 1:
                start = time.perf_counter()
                algo(test_array)
                end = time.perf_counter()
            elif num_args == 3:
                n = len(test_array)-1
                start = time.perf_counter()   
                algo(test_array,0,n)    
                end = time.perf_counter()
            else:
                continue
            duration += end - start

        saving_result(i,duration,j)   
        
