'''Merge Two Sorted Arrays

The approach is similar to the merge subroutine of merge sort.

Time Complexity: O(n1 + n2)
Space Complexity: O(n1 + n2)
'''

def merge_sorted_arrays(arr1, arr2):
    arr3 = [None] * (len(arr1) + len(arr2))
    i, j, k = 0, 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i += 1
        else:
            arr3[k] = arr2[j]
            j += 1
        k += 1

    while i < len(arr1):
        arr3[k] = arr1[i]
        i += 1
        k += 1

    while j < len(arr2):
        arr3[k] = arr2[j]
        j += 1
        k += 1

    return arr3
