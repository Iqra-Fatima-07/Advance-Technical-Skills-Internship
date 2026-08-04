class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def split_list(head):
    if not head or not head.next:
        return head, None

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    head2 = slow.next
    slow.next = None

    return head, head2

def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

print("Original:")
print_list(head)

first_half, second_half = split_list(head)

print("First Half:")
print_list(first_half)
print("Second Half:")
print_list(second_half)
