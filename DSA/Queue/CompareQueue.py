# Question: Write a Python program to compare two queues and determine whether they contain the same elements in the same order.
# Example: Queue 1: 10 20 30, Queue 2: 10 20 30 -> Output: Queues are Equal

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

def are_queues_equal(q1, q2):
    curr1 = q1.front
    curr2 = q2.front
    while curr1 is not None and curr2 is not None:
        if curr1.data != curr2.data:
            return False
        curr1 = curr1.next
        curr2 = curr2.next
    return curr1 is None and curr2 is None

q1 = Queue()
for x in [10, 20, 30]:
    q1.enqueue(x)

q2 = Queue()
for x in [10, 20, 30]:
    q2.enqueue(x)

if are_queues_equal(q1, q2):
    print("Queues are Equal")
else:
    print("Queues are Not Equal")