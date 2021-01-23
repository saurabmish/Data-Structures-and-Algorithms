'''Kadane's Algorithm

This algorithm is used to find the maximum sum of all subarrays in a
contiguous subarray.

Consider A to be the integer array and B to be the contiguous subarray.
If the maximum subarray ends at index i, and sums to B[i], then there
are two possibilities for the maximum subarray to end at index j
(j > i):

1. It is the element at A[j], or
2. It includes earlier entries, i.e, B[i-1] + A[i]

Therefore, B[i] = max(A[i], A[i] + B[i-1])

Consider sequence A: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
The maximum sum subarray starts from A[3] and ends at A[6]
These indices consists of the elements: 4, -1, 2, and 1.
And their sum is 6

Time Complexity:  O(n)
Space Complexity: O(1)
'''

def maximum_sum_subarray(integer_array):
    current_sum, maximum_sum = 0, float('-inf')
    for integer in integer_array:
        current_sum = max(integer, integer + current_sum)
        maximum_sum = max(current_sum, maximum_sum)
    return maximum_sum
