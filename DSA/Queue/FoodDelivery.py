# Question: Mini Project 3: Food Delivery Order Management System using Queue and Stack.
# Features: Place Order, Deliver Order, View Pending Orders, View Delivered Orders, View Last Delivered Order, Exit.

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
        if self.is_empty():
            print("No pending orders.")
            return
        curr = self.front
        while curr:
            print(f"- {curr.data}")
            curr = curr.next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        return temp.data

    def peek(self):
        return self.top.data if self.top else None

    def is_empty(self):
        return self.top is None

    def display(self):
        if self.is_empty():
            print("No delivered orders.")
            return
        curr = self.top
        while curr:
            print(f"- {curr.data}")
            curr = curr.next

class FoodDeliverySystem:
    def __init__(self):
        self.pending_orders = Queue()
        self.delivered_orders = Stack()

    def place_order(self, order_details):
        self.pending_orders.enqueue(order_details)
        print(f"Order placed: '{order_details}'")

    def deliver_order(self):
        if self.pending_orders.is_empty():
            print("No pending orders to deliver.")
            return
        order = self.pending_orders.dequeue()
        self.delivered_orders.push(order)
        print(f"Delivered order: '{order}'")

    def view_pending_orders(self):
        print("Pending Orders:")
        self.pending_orders.display()

    def view_delivered_orders(self):
        print("Delivered Orders (Most recent first):")
        self.delivered_orders.display()

    def view_last_delivered_order(self):
        last = self.delivered_orders.peek()
        if last:
            print(f"Last Delivered Order: '{last}'")
        else:
            print("No delivered orders found.")

def menu():
    system = FoodDeliverySystem()
    while True:
        print("\n--- Food Delivery Order Management System ---")
        print("1. Place Order")
        print("2. Deliver Order")
        print("3. View Pending Orders")
        print("4. View Delivered Orders")
        print("5. View Last Delivered Order")
        print("6. Exit")
        choice = input("Enter choice (1-6): ")

        if choice == '1':
            order = input("Enter order details: ")
            system.place_order(order)
        elif choice == '2':
            system.deliver_order()
        elif choice == '3':
            system.view_pending_orders()
        elif choice == '4':
            system.view_delivered_orders()
        elif choice == '5':
            system.view_last_delivered_order()
        elif choice == '6':
            print("Exiting system.")
            break
        else:
            print("Invalid choice, try again.")

menu()