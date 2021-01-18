## Array vs Linked List

Abstract data types like *stack* and *queue* can be implemented using either an *array* or a *linked list*.

An array consists of a contiguous (long and uninterrupted) block of memory. A linked list consists of individual nodes linked by pointers. Nodes contain data in memory blocks which are not contiguous, and pointers point to these different memory blocks linking the nodes (and making it look as continuous data).

**Memory Allocation**

When a stack or queue is implemented using an array, it has to be allocated a predefined space in memory. And it is quite difficult to get an idea of how much space they would need. This could likely to be a problem either if a large amount of space allocated to them goes unused, or if the amount of space allocated to them runs out. In case of the later, a *dynamic* operation like resizing would have to be performed.
But resizing an array is a costly operation - first, a *bigger* new array has to be created, and then the contents of the current array have to be copied into the new array. If the new array is twice as big as the current array, the total cost of resizing would be roughly *three* times as much. A linked list is dynamic because of nodes (which may increase or decrease) and pointers. There is no such thing as resizing a linked list.

**ADT Operations**

Performing common stack and queue operations (like `push`, `pop`, `enqueue`, `dequeue`, `peek`, etc.) will *always* take more memory when a linked list is used because each node needs to contain a pointer to the next node.
Depending on the kind of data in the node there can be significant overhead. A pointer occupies roughly the same space as an *simple* data type. If a node also contains data of type `int`, it is going to cause a ~ 50% overhead. The data associated with a node should be significantly larger than an `int` data type to reduce the overhead a pointer would cause.

Since all the data is next to each other in an array, there's some empty memory at the end which is used as cache. But in case of a linked list, the effective size of the cache is reduced by the overhead associated with each node - the pointer and unused data space allocated to the node.

**Conclusion**

Using a linked list is a better option when there are few nodes and each of those nodes has a large amount of data. Using an array is a better option when there is a large number of data, each of which is individually small.
