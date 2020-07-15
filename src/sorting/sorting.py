# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # compare the 1st element in both arrays
    for i in range(0, elements):
        if not arrA:
            merged_arr[i] = arrB[0]
            arrB = arrB[1:]
        elif not arrB:
            merged_arr[i] = arrA[0]
            arrA = arrA[1:]
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA[0]
            arrA = arrA[1:]
        else:
            merged_arr[i] = arrB[0]
            arrB = arrB[1:]
    # move the smallest element into the first available position in the merged arr
    # repeat until all elements are in merged array

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    # split array until it's a single item in each array
    # left_index = 0
    # right_index = len(arr)
    # while left_index < right_index:
    #     midpoint = left_index+(right_index)//2
    #     lhs_array = arr[:midpoint]
    #     rhs_array = arr[midpoint:]
    #     merge_sort(lhs_array)
    #     merge_sort(rhs_array)
    #     # merge consecutive arrays back together until there is only 1 array
    #     return merge(lhs_array, rhs_array)

    # return arr
    if len(arr) <= 1:
        return arr
    midpoint = len(arr)//2
    left = merge_sort(arr[:midpoint])
    right = merge_sort(arr[midpoint:])
    arr = merge(left, right)
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
    # Your code here

    # def merge_sort_in_place(arr, l, r):
    # Your code here


# print(merge([1, 2, 3], [4, 3, 8]))
print(merge_sort([1, 5, 2, 7]))
