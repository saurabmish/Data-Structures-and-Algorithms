'''Quick Sort

In-place sorting algorithm.

Time Complexity (likely): O(nlogn)
Space Complexity:         O(logn)
'''

def partition(arr, low, high):
    """Hoare Partition."""
    pivot = arr[(low + high) // 2]
    while True:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1

        if low >= high:
            return high
        arr[low], arr[high] = arr[high], arr[low]
        low += 1; high -= 1

def quicksort(arr, low, high):
    if low < high:
        mid = partition(arr, low, high)
        quicksort(arr, low, mid)
        quicksort(arr, mid + 1, high)
    return arr
