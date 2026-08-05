class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_alt(head):
    if not head:
        return head
    
    curr = head
    while curr and curr.next:
        curr.next = curr.next.next
        curr = curr.next
    return head

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

print_list(head)
head = delete_alt(head)
print_list(head)
