## Keeping Track of Vertices:

**Set**:

The set data structure in Python 3.7+ does not preserve order, because by definition, a set is an unordered collections of unique elements.

Search (or lookup) is constant time, i.e., O(1) Adding an element in a set is faster in most cases than a list.

Creating a set causes more overhead than creating a list. This overhead is directly proportional to the number of elements.

**List**:

A list, by definition, is an ordered collection of elements.

Although sets and lists both have linear time iteration, lists may be *slightly* faster than sets for iterating over values.

Search (or lookup) is linear time - O(n), i.e., directly proportional to the number of elements.

**Conclusion**:

The output of depth first search is not unique and will depend on the traversal path that is selected. Both data structures will perform in a similar manner in the `while` loop, but using a set will provide constant lookup time `O(1)` when `if vertex in visited` is executed. A list will have a linear lookup time of `O(n)`.
**However**, using a list is more intuitive as the first element of the resulting traversal is the same as the starting element provided as an argument.

Using Python's dictionary (from version 3.7+) is another option. It has constant lookup time and preserves order of visited vertices.
