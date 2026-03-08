from .mergesort import merge
from .insertionsort import insertion_sort


def non_optimized_timsort(arr):
    run_length = 32
    n = len(arr)
    for i in range(0, n, run_length):
        end = min(n - 1, i + run_length - 1)
        insertion_sort(arr, i, end)
    size = run_length
    while size < n:
        for i in range(0, n, 2 * size):
            end = min(n - 1, i + 2 * size - 1)
            m = min(n-1,i + size -1)
            merge(arr, i, m, end)
        size *= 2
    return arr

if __name__ =="__main__":
    
    
    arr = [1,51,1,31,1,1,3,3,3,3,3,2,52,52,52,43,24,24,24,24,24,24,14,2,35,435,435,35,24242,4242,141,4]
    non_optimized_timsort(arr)
    print(arr)
