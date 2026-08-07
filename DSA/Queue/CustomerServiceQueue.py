# Question: Write a Python program to implement a Customer Service Queue supporting operations:
# Add Customer, Serve Customer, Display Waiting Customers, Display Front Customer, Display Total Customers.

class Customer:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.next = None

class CustomerServiceQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def add_customer(self, name, id):
        new_cust = Customer(name, id)
        if self.rear is None:
            self.front = self.rear = new_cust
        else:
            self.rear.next = new_cust
            self.rear = new_cust
        self.count += 1
        print(f"Customer {name} (ID: {id}) added.")

    def serve_customer(self):
        if self.front is None:
            print("No customers to serve.")
            return None
        served = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.count -= 1
        print(f"Served Customer: {served.name} (ID: {served.id})")
        return served

    def display_waiting_customers(self):
        if self.front is None:
            print("No waiting customers.")
            return
        curr = self.front
        print("Waiting Customers:")
        while curr:
            print(f"- ID: {curr.id}, Name: {curr.name}")
            curr = curr.next

    def display_front_customer(self):
        if self.front is None:
            print("No customers in line.")
        else:
            print(f"Front Customer: {self.front.name} (ID: {self.front.id})")

    def display_total_customers(self):
        print(f"Total waiting customers: {self.count}")

cs = CustomerServiceQueue()
cs.add_customer("Alice", 101)
cs.add_customer("Bob", 102)
cs.add_customer("Charlie", 103)
cs.display_front_customer()
cs.display_total_customers()
cs.display_waiting_customers()
cs.serve_customer()
cs.display_total_customers()