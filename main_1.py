class Stack():

    def __init__(self, stack):
        self.stack = list(stack)

    def is_empty(self):
        return False if len(self.stack) > 0 else True

    def push(self, item: str):
        self.stack += item

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

