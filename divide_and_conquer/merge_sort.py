'''Merge Sort

Efficient, general-purpose sorting algorithm

Time Complexity: O(nlogn) (best, worst, and average)
Space Complexity: O(n)
'''

import math

def mergesort(int_arr, left, right):
    """Operations

    1. Divide the input array into two halves, and sort each half
       recursively.
    2. Merge the sorted halves
    """
    if left < right:
        mid = (left + right) // 2
        mergesort(int_arr, left, mid)
        mergesort(int_arr, mid + 1, right)
        merge(int_arr, left, mid, right)
    return int_arr

def merge(arr, left, mid, right):
    """Operations

    1. Create two arrays corresponding to the length of the left and
       right subarrays.
    2. Copy left and right subarrays in the newly created subarrays
       ("-inf" is the sentinel value at the end)
    3. Iterate from the left to the right-most element by comparing values
       present in subarrays and overwriting it back to the input array.
    """
    n1 = mid - left + 1
    n2 = right - mid

    low  = [None] * (n1+1)
    high = [None] * (n2+1)

    for i in range(n1):
        low[i]  = arr[left+i]
    for j in range(n2):
        high[j] = arr[mid+1+j]

    low[n1] = high[n2] = math.inf
    i = j = 0

    for k in range(left, right+1):
        if low[i] <= high[j]:
            arr[k] = low[i]
            i += 1
        else:
            arr[k] = high[j]
            j += 1
