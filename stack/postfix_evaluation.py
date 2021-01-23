'''Postfix Expression Evaluation

Consider the below postfix expression:
2 3 1 * + 9 -

Evaluation:
2 (3 * 1) + 9 -
2 3 + 9 -
(2 + 3) 9 -
5 9 -
5 - 9
-4

Time Complexity: O(n)
Space Complexity: O(n)
'''

def postfix_evaluation(expression):
    """Operations:

    1. Push the operand on stack.
    2. Evaluate the expression when an operator is indexed by using
       the two recently added operands on stack
    3. Push the result to the stack
    """
    stack = []
    for index in expression:
        if index.isdigit():
            stack.append(index)
        else:
            val1, val2 = stack.pop(), stack.pop()
            compute = str(eval(val2 + index + val1))
            stack.append(compute)
    return stack.pop()
