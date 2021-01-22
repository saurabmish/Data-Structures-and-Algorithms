'''Longest Increasing Subsequence

A subsequence is a sequence that can be derived from an array by
deleting some or no elements, without changing the order of the
remaining elements.

Consider the sequence: [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
Length of the LIS is 4, which can be obtained by deleting:
8, 12, 2, 6, 1, and 9.
So the longest subsequence consists of elements: 0, 4, 10, 14

Time Complexity:  O(n^2)
Space Complexity: O(n)
'''

def longest_increasing_subsequence(integer_array):
    """Return length of the longest increasing subsequence."""
    if integer_array is None or len(integer_array) == 0:
        raise ValueError("Input sequence not provided ...")

    length = [1] * len(integer_array)
    for i in range(1, len(integer_array)):
        for j in range(0, i):
            if integer_array[i] > integer_array[j]:   # >= for non-decreasing
                length[i] = max(length[j] + 1, length[i])

    return max(length)
