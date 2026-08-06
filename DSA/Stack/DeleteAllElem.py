class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def display(self):
        print("Stack:", self.stack)

def delete_all(original_stack):
    while not original_stack.is_empty():
        original_stack.pop()

s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Before deleting:")
s.display()
delete_all(s)
print("After deleting:")
s.display()
