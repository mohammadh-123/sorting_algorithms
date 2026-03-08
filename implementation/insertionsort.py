def insertion_sort(arr, l, r):
    
    for i in range(l + 1, r + 1):
        j = i - 1
        element = arr[i]
        while j >= l and arr[j] > element:

            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = element
    return arr

if __name__ == "__main__":
    arr = [1, 2, 2, 1, 5, 3, 12, 3]

    print(insertion_sort(arr, 0, len(arr) - 1))
