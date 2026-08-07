# Question: Write a Python program to rotate a queue by K positions.
# Example: Queue: 10 20 30 40 50, K = 2 -> Output: 30 40 50 10 20

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1

    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        self.length -= 1
        return temp.data

    def is_empty(self):
        return self.front is None

    def display(self):
        curr = self.front
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(" ".join(elements))

def rotate_queue(q, k):
    if q.is_empty() or q.length == 0:
        return
    k = k % q.length
    for _ in range(k):
        val = q.dequeue()
        q.enqueue(val)

q = Queue()
for x in [10, 20, 30, 40, 50]:
    q.enqueue(x)

k = 2
rotate_queue(q, k)
print("Output:")
q.display()