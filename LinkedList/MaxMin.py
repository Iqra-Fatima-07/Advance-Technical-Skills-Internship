#Program to find maximum and minimum in a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def find_max_min(self):
        max_val = float('-inf')
        min_val = float('inf')

        current = self.head
        while current:
            if current.data > max_val:
                max_val = current.data
            if current.data < min_val:
                min_val = current.data
            current = current.next

        return max_val, min_val

# Example usage
llist = LinkedList()
llist.insert(5)
llist.insert(2)
llist.insert(8)
llist.insert(1)
llist.insert(3)

max_val, min_val = llist.find_max_min()
print("Maximum value:", max_val)
print("Minimum value:", min_val)