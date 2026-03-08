def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

if __name__ == "__main__":
    
    arr = [1,2,2,1,5,3,12,3]

    print(selection_sort(arr))