# Question: Write a Python program to merge two queues into a single queue while preserving the order of elements.
# Example: Queue 1: 10 20 30, Queue 2: 40 50 60 -> Output: 10 20 30 40 50 60

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
        print(" ".join(elements))

def merge_queues(q1, q2):
    merged = Queue()
    while not q1.is_empty():
        merged.enqueue(q1.dequeue())
    while not q2.is_empty():
        merged.enqueue(q2.dequeue())
    return merged

q1 = Queue()
for x in [10, 20, 30]:
    q1.enqueue(x)

q2 = Queue()
for x in [40, 50, 60]:
    q2.enqueue(x)

merged_q = merge_queues(q1, q2)
print("Output:")
merged_q.display()