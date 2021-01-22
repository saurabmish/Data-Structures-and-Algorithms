'''Quick Sort

In-place sorting algorithm.

Time Complexity: O(nlogn)
Space Complexity: O(logn)
'''

def partition(arr, low, high):
    """Hoare Partition."""
    pivot = arr[(low+high) // 2]
    i = low
    j = high
    while i < j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def quicksort(arr, low, high):
    if low < high:
        mid = partition(arr, low, high)
        quicksort(arr, low, mid)
        quicksort(arr, mid + 1, high)
    return arr

def main():
    integer_array = [-2, 0, 32, 1, 56, 99, -4]
    print(quicksort(integer_array, 0, len(integer_array) - 1))

if __name__ == '__main__':
    main()
