class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def get_sum(head):
    total_sum = 0
    curr = head
    while curr:
        total_sum += curr.data
        curr = curr.next
    return total_sum

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print("Sum of nodes:", get_sum(head))
