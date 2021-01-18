## Stability in Sorting Algorithms

A sorting algorithm is said to be stable if two objects with equal keys appear in the same order in sorted output as they appear in the input array to be sorted.

In simpler words, a stable sorting algorithm keeps the items with the same sorting key in order of their input.

Consider the following words:
*peach, straw, apple, spark*

Sorting by the first letter in a stable manner:
*apple, peach, straw, spark*

Sorting by the first letter in an unstable manner:
*apple, peach, spark, straw*

**NOTE**: In an unstable sort algorithm, *straw* or *spark* may be
interchanged, but in a stable one, they stay in the same relative
positions.

**Usefulness of Stability**

*Scenario 1*:

Stable sorting can be used to 'chain' through multiple conditions. In a practical situation, this could be when a user clicks on a column to sort, and then clicks on another column to sort further.

Assume that there's a list of first and last names. The requirement is to sort by last name, then by first. The first name can be sorted first, followed by the last name. At this point, the list is primarily sorted by the last name. However, in cases where last names of two or more people are the same, they will be sorted by their first names.

*Scenario 2*:

Say you have a data structure that contains pairs of phone numbers and employees who called them. A number/employee record is added after each call. Some phone numbers may be called by several different employees.

Furthermore, say you want to sort the list by phone number and give a bonus to the first 2 people who called any given number.

If you sort with an unstable algorithm, you may not preserve the order of callers of a given number, and the wrong employees could be given the bonus.

A stable algorithm makes sure that the right 2 employees per phone number get the bonus.

**Examples**

*Stable*:

Bubble Sort
Insertion Sort
Counting Sort
Merge Sort

*Unstable*:

Heap sort
Selection sort
Shell sort
Quick sort
