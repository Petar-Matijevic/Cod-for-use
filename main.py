# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def binary_search(arr,target):
    low,high =0,len(arr) - 1

    while low<=high:
        mid=(low+high)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid +1
        else:
            high = mid -1

    return -1



if __name__ == '__main__':
    sorted_array = [1,2,3,4,5,6,7,8,9,10]
    target_value = 5
    result = binary_search(sorted_array,target_value)
    if result != -1:
        print(f"Element {target_value} is present at index {result}.")
    else:
        print(f"Element {target_value} is not present in the array.")
# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
