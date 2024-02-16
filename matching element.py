def find_matching_element(arr1,arr2):
    return list(set(arr1)&set(arr2))

array1 = [1,2,3,4,5]
array2 = [3, 4, 5, 6, 7]
print(find_matching_element(array1, array2))