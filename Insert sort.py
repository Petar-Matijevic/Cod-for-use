def insert_sort(arr):
    for i in range(1,len(arr)):
        n =arr[i]
        j = i-1
        while j >= 0 and n <arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1]=n



input_array = [64, 34, 25, 12, 22, 11, 90]
insert_sort(input_array)
print("Sorted array:", input_array)