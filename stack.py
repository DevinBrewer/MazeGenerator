from node import Node

class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        # Return the True/False state of the Stack
        return len(self.stack) == 0

    def push(self, node):
        # Append the x, y of a new node
        self.stack.append(node)

    def pop(self):
        # Remove the last value in the stack
        self.stack.pop()

    def getActive(self):
        return self.stack[-1]
