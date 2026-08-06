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

def reverse_stack(original_stack):
    temp1 = Stack()
    temp2 = Stack()
    
    while not original_stack.is_empty():
        temp1.push(original_stack.pop())
        
    while not temp1.is_empty():
        temp2.push(temp1.pop())
        
    while not temp2.is_empty():
        original_stack.push(temp2.pop())

s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Original:")
s.display()
reverse_stack(s)
print("Reversed:")
s.display()
