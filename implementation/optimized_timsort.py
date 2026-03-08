from .mergesort import merge
from .insertionsort import insertion_sort

def calc_min_run(n):
    min_run = 32
    r = 0
    while n >= min_run:
        r |= n & 1 # checking for odd numbers and store the leat important bit
        n >>= 1 # same as n //= 2 but this is bit operator and it is faster
    return n + r

def find_run(arr,s):
    n = len(arr)
    e = s + 1
    if e == n:
        return e
    if arr[e] < arr[e-1]:
        while e < n and arr[e]<arr[e-1]:
            e += 1
        arr[s:e] = reversed(arr[s:e])
    else:
        while e < n and arr[e] >= arr[e-1]:
            e += 1
    return e

def calc_run_length(run):
    s,e = run
    return e - s
        
def merge_two_runs(arr,runs,i1,i2):
    start = runs[i1][0]
    end = runs[i2][1]
    m = runs[i1][1]-1
    merge(arr,start,m,end -1)
    runs[i1] = (start,end)
    runs.pop(i2)
    
def optimized_timsort(arr):
    n = len(arr)
    min_run = calc_min_run(n)
    i = 0
    runs = []
    while i < n:
        run_end = find_run(arr,i)
        run_length = run_end - i
        if min_run > run_length:
            run_end = min(n , i + min_run)
            insertion_sort(arr,i,run_end-1)
        runs.append((i,run_end))
        i = run_end
        while len(runs) > 1:
            
            if len(runs) > 2 and calc_run_length(runs[-3]) <= calc_run_length(runs[-2]) + calc_run_length(runs[-1]):
                if calc_run_length(runs[-3]) < calc_run_length(runs[-1]):
                    merge_two_runs(arr,runs,-3,-2)
                else:
                    merge_two_runs(arr,runs,-2,-1)
            elif calc_run_length(runs[-2]) <= calc_run_length(runs[-1]):
                merge_two_runs(arr,runs,-2,-1)
            else:
                break
    while len(runs) > 1:
        merge_two_runs(arr,runs,-2,-1)

    return arr
if __name__ =="__main__":
    arr = [1,51,1,31,1,1,3,3,3,3,3,2,52,52,52,43,24,24,24,24,24,24,14,2,35,435,435,3,2,1,4,3,3,3,3,3,3,2,66,4,5,1,4,3,2,3,4,3,5,3,3,2,5,54,5,242,42,3,42,342,12,3,43,2,42,3,42,34,1,3,5,24242,4242,141,4]
    optimized_timsort(arr)
    print(arr)