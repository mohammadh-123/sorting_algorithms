def merge(arr,s,m,e):
    n1 = m-s+1
    n2 = e-m
    l = arr[s:m+1]
    r = arr[m+1:e+1]
    i,j = 0,0
    k = s
    while i<n1 and j<n2:
        if l[i] <= r[j]:
            arr[k] = l[i]
            i+=1
        else:
            arr[k] = r[j]
            j+=1
        k+=1        
    if i < n1:
        arr[k:e+1] = l[i:]

    if j< n2:
        arr[k:e+1] = r[j:]
def merge_sort(arr,s,e):
    if s >= e:
        return arr
    m = s + (e - s) // 2
    merge_sort(arr,s,m)
    merge_sort(arr,m+1,e)
    merge(arr,s,m,e)
    return arr

if __name__ =='__main__':
    
    arr = [1,51,1,31,1,1,3,3,3,3,3,2,52,52,52,43,24,24,24,24,24,24,14,2,35,435,435,3,2,1,4,3,3,3,3,3,3,2,66,4,5,1,4,3,2,3,4,3,5,3,3,2,5,54,5,242,42,3,42,342,12,3,43,2,42,3,42,34,1,3,5,24242,4242,141,4]

    print(merge_sort(arr,0,len(arr)-1))
    
    
    