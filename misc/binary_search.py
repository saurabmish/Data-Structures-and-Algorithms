'''Binary Search

Takes a sorted list and tries to find the target by reducing the search
scope in half every iteration. This is done by adjusting the upper or
lower bound is adjusted with the middle index of input array, depending
on the target.
An array of 8 elements would require 4 guesses at most,
An array of 6 elements would require 3 guesses at most, and so on

Time Complexity:  O(logn)
Space Complexity: O(1)
'''

def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)
