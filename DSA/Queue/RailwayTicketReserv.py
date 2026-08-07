# Question: Mini Project 1: Railway Ticket Reservation System using Queue and Stack.
# Features: Add Passenger to Waiting Queue, Book Ticket (Serve Passenger), Cancel Ticket, View Waiting Passengers, View Last Cancelled Ticket, Exit.

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
            print("No waiting passengers.")
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

class RailwayReservationSystem:
    def __init__(self):
        self.waiting_queue = Queue()
        self.cancellation_stack = Stack()
        self.booked_passengers = []

    def add_passenger(self, name):
        self.waiting_queue.enqueue(name)
        print(f"Passenger '{name}' added to waiting queue.")

    def book_ticket(self):
        if self.waiting_queue.is_empty():
            print("No passengers in waiting queue to book ticket.")
            return
        passenger = self.waiting_queue.dequeue()
        self.booked_passengers.append(passenger)
        print(f"Ticket booked successfully for '{passenger}'.")

    def cancel_ticket(self, name):
        if name in self.booked_passengers:
            self.booked_passengers.remove(name)
            self.cancellation_stack.push(name)
            print(f"Ticket cancelled for '{name}'.")
        else:
            print(f"Passenger '{name}' not found in booked tickets.")

    def view_waiting_passengers(self):
        print("Waiting Passengers:")
        self.waiting_queue.display()

    def view_last_cancelled(self):
        last = self.cancellation_stack.peek()
        if last:
            print(f"Last Cancelled Ticket: '{last}'")
        else:
            print("No cancellations recorded.")

def menu():
    system = RailwayReservationSystem()
    while True:
        print("\n--- Railway Ticket Reservation System ---")
        print("1. Add Passenger to Waiting Queue")
        print("2. Book Ticket (Serve Passenger)")
        print("3. Cancel Ticket")
        print("4. View Waiting Passengers")
        print("5. View Last Cancelled Ticket")
        print("6. Exit")
        choice = input("Enter choice (1-6): ")

        if choice == '1':
            name = input("Enter passenger name: ")
            system.add_passenger(name)
        elif choice == '2':
            system.book_ticket()
        elif choice == '3':
            name = input("Enter passenger name to cancel: ")
            system.cancel_ticket(name)
        elif choice == '4':
            system.view_waiting_passengers()
        elif choice == '5':
            system.view_last_cancelled()
        elif choice == '6':
            print("Exiting system.")
            break
        else:
            print("Invalid choice, try again.")

menu()