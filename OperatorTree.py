# Operator Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Check if the character is an operator
def isOperator(ch):
    return ch in ['+', '-', '*', '/']

# Generate an expression tree from the postfix expression
def gen_exp(exp):
    stack = []

    # Traverse the postfix expression
    for i in exp:
        # If the character is an operand, create a node and push it to the stack
        if not isOperator(i):
            temp = Node(i)
            stack.append(temp)
        else:
            # If it's an operator, pop two elements and create a node
            right = stack.pop()
            left = stack.pop()
            temp = Node(i)
            temp.left = left
            temp.right = right
            stack.append(temp)

    # The last element in the stack is the root of the expression tree
    return stack.pop()

# Inorder traversal (left, root, right)
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end="")
    inorder(root.right)

# Postorder traversal (left, right, root)
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end="")

# Evaluate the expression tree
def eval_tree(root):
    if root is None:
        return 0

    # If the node is an operand, return its value
    if root.data.isdigit():
        return int(root.data)

    # If the node is an operator, evaluate the left and right subtrees
    left = eval_tree(root.left)
    right = eval_tree(root.right)

    # Apply the operator
    if root.data == '+':
        return left + right
    elif root.data == '-':
        return left - right
    elif root.data == '*':
        return left * right
    elif root.data == '/':
        return left / right

# Example usage
postfix_expr = "12*34/+"
root = gen_exp(postfix_expr)

# Inorder Expression Tree: It should give the infix expression
print("Inorder Expression:", end=" ")
inorder(root)
print()

# Postorder Expression Tree: It should give the postfix expression
print("Postorder Expression:", end=" ")
postorder(root)
print()

# Evaluating the expression tree
result = eval_tree(root)
print("Evaluated Result:", result)
