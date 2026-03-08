def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        
        r = True
        for j in range(n-i-1): 
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                r = False
        if r:
            break
    return arr

if __name__ =="__main__":
    
    arr = [4,3,2,1]
    print(bubble_sort(arr))
