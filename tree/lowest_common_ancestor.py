'''Lowest Common Ancestor of Two Nodes

The idea is to traverse upward from each node towards the root node
while keeping track of the visited node(s). Since upward traversal
requires each node to know its parent, we do an initial depth-first
search to find the parent of each node.

Time Complexity:  O(n)
Space Complexity: O(n)
'''

from .node import BinaryNode

def lca(root, node1, node2):
    """Operations:

    1. Start traversal from root
    2. Store parent pointers for each node until node1 and node2 are found
    3. Once both nodes are found,
       a) Get ancestors of node1 from dictionary and add to set
       b) Check if any ancestor of node1 is present in node2's parent. If
          they do have a common ancestor, it is the first (lowest) common
          ancestor of both nodes
    """
    stack, parent = [], {root: None}
    ancestors = set()
    stack.append(root)

    while node1 not in parent or node2 not in parent:
        current = stack.pop()
        if current.left:
            parent[current.left] = current
            stack.append(current.left)
        if current.right:
            parent[current.right] = current
            stack.append(current.right)

    while node1:
        ancestors.add(node1)
        node1 = parent[node1]
    while node2 not in ancestors:
        node2 = parent[node2]

    return node2.key
