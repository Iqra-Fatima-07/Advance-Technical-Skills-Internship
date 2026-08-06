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

def copy_stack(source_stack):
    temp_stack = Stack()
    destination_stack = Stack()
    
    while not source_stack.is_empty():
        temp_stack.push(source_stack.pop())
        
    while not temp_stack.is_empty():
        item = temp_stack.pop()
        source_stack.push(item)
        destination_stack.push(item)
        
    return destination_stack

s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)

s2 = copy_stack(s1)
print("Source:")
s1.display()
print("Copied Destination:")
s2.display()
