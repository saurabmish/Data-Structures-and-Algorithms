''' K-th Smallest Element

Find the k-th smallest element in an array, assuming that the entries
are distinct and unsorted.

The quick select algorithm is used to find the k-th largest value in an
unsorted list. It is very similar to quick sort algorithm.

Worst-case is O(n*n) and happens when the pivot is the smallest or
largest value in the sub-array. The probability of worst-case reduces
exponentially with the length of the array, thereby making the worst-
case a non-issue.

Time Complexity:  O(n)
Space Complexity: O(logn)
'''

import random

def partitian(arr, left, right, pivot_index):
    """Lomuto Partition."""
    pivot_val = arr[pivot_index]
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    store_index = left
    for i in range(left, right):
        if arr[i] < pivot_val:      # change to > for largest
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
    arr[store_index], arr[right] = arr[right], arr[store_index]
    return store_index

def select(arr, left, right, k):
    while True:
        if left == right:
            return arr[left]
        pivot_index = random.randint(left, right)
        pivot_index = partitian(arr, left, right, pivot_index)
        if pivot_index == k-1:
            return arr[k-1]
        elif k-1 < pivot_index:
            right = pivot_index - 1
        else:
            left = pivot_index + 1

