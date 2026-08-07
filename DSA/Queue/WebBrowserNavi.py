# Question: Mini Project 2: Web Browser Navigation System using Stack and Queue.
# Features: Visit New Page, View Browsing History, Back, View Last Visited Page, Exit.

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

    def is_empty(self):
        return self.front is None

    def display(self):
        if self.is_empty():
            print("Browsing history is empty.")
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

class WebBrowserNavigation:
    def __init__(self):
        self.history_queue = Queue()
        self.back_stack = Stack()
        self.current_page = None

    def visit_page(self, url):
        if self.current_page:
            self.back_stack.push(self.current_page)
        self.current_page = url
        self.history_queue.enqueue(url)
        print(f"Visited: {url}")

    def view_history(self):
        print("Browsing History (Order of Visit):")
        self.history_queue.display()

    def back(self):
        if self.back_stack.is_empty():
            print("No previous page to go back to.")
            return
        prev = self.back_stack.pop()
        self.current_page = prev
        print(f"Went back to: {self.current_page}")

    def view_last_visited(self):
        if self.current_page:
            print(f"Current/Last Visited Page: {self.current_page}")
        else:
            print("No pages visited yet.")

def menu():
    browser = WebBrowserNavigation()
    while True:
        print("\n--- Web Browser Navigation System ---")
        print("1. Visit New Page")
        print("2. View Browsing History")
        print("3. Back")
        print("4. View Last Visited Page")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")

        if choice == '1':
            url = input("Enter webpage URL: ")
            browser.visit_page(url)
        elif choice == '2':
            browser.view_history()
        elif choice == '3':
            browser.back()
        elif choice == '4':
            browser.view_last_visited()
        elif choice == '5':
            print("Exiting browser.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()