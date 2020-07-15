# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # starting pointer
    # start = arr[0]
    # # end Pointer
    # end = len(arr)-1
    # find midpoint
    midpoint = (end+start)//2
    if end < start:
        return -1
    # base case
    if arr[midpoint] == target:
        return midpoint
    # recursive case
    elif target < arr[midpoint]:
        end = midpoint - 1
        return binary_search(arr, target, start, end)
    elif target > arr[midpoint]:
        start = midpoint + 1
        return binary_search(arr, target, start, end)
    return -1
    # STRETCH: implement an order-agnostic binary search
    # This version of binary search should correctly find
    # the target regardless of whether the input array is
    # sorted in ascending order or in descending order
    # You can implement this function either recursively
    # or iteratively


# def agnostic_binary_search(arr, target):
    # Your code here


arr1 = [3, 7, 11, 14, 20]

print(binary_search(arr1, -8, 0, len(arr1)-1))
