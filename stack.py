class Stack:
    def __init__(self):
        self.stack = []
        self.iterations = 0

    def stack_push(self, data):
        self.stack.append(data)
        self.iterations += 1

    def stack_pop(self):
        self.iterations += 1
        if self.stack is None:
            print("Stack is empty")
        else:
            return self.stack.pop()

    def stack_peek(self):
        print(f"Stack looks like this after")
        print(self.iterations)
        print("iterations")
        for data in self.stack:
            print(data)


stack = Stack()

stack.stack_push('Mon')
stack.stack_push('Tue')

stack.stack_peek()

stack.stack_push('Wed')
stack.stack_push('Thu')

stack.stack_peek()

stack.stack_pop()
stack.stack_pop()
stack.stack_pop()
stack.stack_peek()
