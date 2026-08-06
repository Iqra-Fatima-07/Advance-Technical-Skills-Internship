class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0


class TextEditor:
    def __init__(self):
        self.current_text = ""
        self.history_stack = Stack()

    def add_text(self, new_text):
        self.history_stack.push(self.current_text)
        if self.current_text:
            self.current_text += " " + new_text
        else:
            self.current_text = new_text
        print(f'Text "{new_text}" added successfully.')

    def display_text(self):
        if not self.current_text:
            print("--- Text Editor is Empty ---")
        else:
            print("\n--- Current Text ---")
            print(self.current_text)
            print("--------------------\n")

    def undo(self):
        if self.history_stack.is_empty():
            print("Nothing to Undo! No previous states available.")
            return

        self.current_text = self.history_stack.pop()
        print("Undo operation successful.")


def main():
    editor = TextEditor()

    while True:
        print("=== Text Editor Operations ===")
        print("1. Add new text")
        print("2. Display current text")
        print("3. Undo last operation")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.\n")
            continue

        if choice == 1:
            text_to_add = input("Enter the text to add: ")
            editor.add_text(text_to_add)
        elif choice == 2:
            editor.display_text()
        elif choice == 3:
            editor.undo()
        elif choice == 4:
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid menu option.\n")


if __name__ == "__main__":
    main()
