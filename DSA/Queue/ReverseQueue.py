# Question: Write a Python program to reverse all elements of a queue without using the built-in reverse() method.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def is_empty(self):
        return self.front is None

    def display(self):
        curr = self.front
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(elements))

def reverse_queue(q):
    if q.is_empty():
        return
    val = q.dequeue()
    reverse_queue(q)
    q.enqueue(val)

q = Queue()
for x in [10, 20, 30, 40, 50]:
    q.enqueue(x)

print("Original Queue:")
q.display()

reverse_queue(q)

print("Reversed Queue:")
q.display()