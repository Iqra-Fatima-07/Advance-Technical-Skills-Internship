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

def search_element(original_stack, target):
    temp_stack = Stack()
    found = False
    
    while not original_stack.is_empty():
        item = original_stack.pop()
        temp_stack.push(item)
        if item == target:
            found = True
            
    while not temp_stack.is_empty():
        original_stack.push(temp_stack.pop())
        
    return found

s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Element found:", search_element(s, 20))
