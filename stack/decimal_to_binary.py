'''Decimal to its Binary Equivalent

Valid for non-negative integers.

Time Complexity: O(n)
Space Complexity: O(n)
'''

def decimal_to_binary(decimal):
    """Operations:

    1. Divide the number by 2 and push the remainder to stack
    2. The number then becomes half of its original decimal value
    3. Binary representation is obtained by popping the stack (LIFO)
    """
    stack = []
    while decimal > 0:
        remainder = decimal % 2
        stack.append(remainder)
        decimal = decimal // 2

    binary = ""
    while stack:
        binary += str(stack.pop())

    return binary
