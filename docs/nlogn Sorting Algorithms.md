## Quick Sort

*Worst Case*: O(n^2)

*Average Case*: O(nlogn)

Quick sort will exhibit worst case performance when *the* most unbalanced partition is produced. This happens when one of the sublists returned by the `partition` routine is of size (n − 1). This may happen if the pivot happens to be the smallest or largest element.

To reduce the possibility of the pivot being the smallest or largest element, a random element should be chosen as pivot. The code in this repository uses the middle element as the pivot. Other options include selecting a random element as pivot, or choosing the median of the first, middle and last element as pivot.

Best case is when a balanced partition is produced - both sublists are nearly equal size.
Quick sort is an in-place sorting algorithm and does not require extra space. This is because the positions of data is swapped in the `partition` function.
