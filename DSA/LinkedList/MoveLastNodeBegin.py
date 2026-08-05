class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def move_last_to_front(head):
    if not head or not head.next:
        return head
    
    sec_last = None
    last = head
    
    while last.next:
        sec_last = last
        last = last.next
        
    sec_last.next = None
    last.next = head
    head = last
    
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
head = move_last_to_front(head)
print_list(head)
