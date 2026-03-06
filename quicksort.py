def partition(arr,l,r):
    n = len(arr)
    pivolt = arr[r]
    j = l
    for i in range(l,r):
        if arr[i]<pivolt:
            arr[i],arr[j] = arr[j],arr[i]
            j += 1
    arr[r],arr[j] = arr[j],arr[r]
    return j
    
    
def quicksort(arr,l,r):
    if l>=r:
        return arr
    pivolt = partition(arr,l,r)
    quicksort(arr,l,pivolt-1)
    quicksort(arr,pivolt+1,r)
    return arr

arr = [1,2,2,1,5,3,12,3]

print(quicksort(arr,0,len(arr)-1))
    
    