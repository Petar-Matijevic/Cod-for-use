def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1]=arr[j+1], arr[j]

input_array = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(input_array)
print("Sorted array:", input_array)