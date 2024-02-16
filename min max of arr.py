def returnminmax(arr):
    if len(arr)==0:
        return  None,None
    else:
        return  max(arr),min(arr)
input_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
largest, smallest = returnminmax(input_array)
print("Largest element:", largest)  # Output: 9
print("Smallest element:", smallest)