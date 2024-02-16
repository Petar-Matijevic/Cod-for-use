def second_largest(arr):
    # Ensure the array has at least two elements
    if len(arr) < 2:
        return "Array should have at least two elements"

    largest = float('-inf')  # Initialize largest as negative infinity
    second_largest = float('-inf')  # Initialize second largest as negative infinity

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return "There is no second largest element"
    else:
        return second_largest

# Example usage
arr = [12, 35, 1, 10, 34, 1]
result = second_largest(arr)
print("Second largest element:", result)