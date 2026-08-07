# Question: Write a Python program to separate the elements of a queue into two different queues: Even Queue and Odd Queue.

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
        print(" -> ".join(elements) if elements else "Empty")

def separate_even_odd(q):
    even_q = Queue()
    odd_q = Queue()
    while not q.is_empty():
        val = q.dequeue()
        if val % 2 == 0:
            even_q.enqueue(val)
        else:
            odd_q.enqueue(val)
    return even_q, odd_q

q = Queue()
for x in [12, 7, 9, 24, 18, 5, 30]:
    q.enqueue(x)

even_q, odd_q = separate_even_odd(q)

print("Even Queue:")
even_q.display()
print("Odd Queue:")
odd_q.display()