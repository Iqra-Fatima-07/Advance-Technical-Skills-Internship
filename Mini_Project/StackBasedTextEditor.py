import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class TextEditor:

    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Stack Based Text Editor")
        self.root.geometry("1200x750")
        self.root.minsize(1000, 650)

        self.undo_stack = [""]
        self.redo_stack = []
        self.last_saved_state = ""
        self.debounce_timer = None

        self.build_ui()

    def build_ui(self):
        title = ctk.CTkLabel(
            self.root,
            text="📄 Stack Based Text Editor",
            font=("Segoe UI", 30, "bold")
        )
        title.pack(pady=20)

        main = ctk.CTkFrame(self.root, fg_color="transparent")
        main.pack(fill="both", expand=True, padx=20, pady=10)

        left = ctk.CTkFrame(main)
        left.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        right = ctk.CTkFrame(main, width=280)
        right.pack_propagate(False)
        right.pack(side="right", fill="y", padx=10, pady=10)

        self.textbox = ctk.CTkTextbox(
            left,
            font=("Consolas", 16),
            wrap="word",
            undo=False
        )
        self.textbox.pack(fill="both", expand=True, padx=15, pady=15)

        self.textbox.bind("<KeyRelease>", self.handle_key_release)

        btn_frame = ctk.CTkFrame(left, fg_color="transparent")
        btn_frame.pack(fill="x", padx=15, pady=(0, 15))

        self.undo_btn = ctk.CTkButton(
            btn_frame,
            text="↩ Undo",
            fg_color="#10B981",
            hover_color="#059669",
            command=self.undo,
            width=100
        )

        self.redo_btn = ctk.CTkButton(
            btn_frame,
            text="↪ Redo",
            fg_color="#3B82F6",
            hover_color="#2563EB",
            command=self.redo,
            width=100
        )

        clear_btn = ctk.CTkButton(
            btn_frame,
            text="🗑 Clear",
            fg_color="#EF4444",
            hover_color="#DC2626",
            command=self.clear_text,
            width=100
        )

        exit_btn = ctk.CTkButton(
            btn_frame,
            text="🚪 Exit",
            fg_color="#9333EA",
            hover_color="#7E22CE",
            command=self.exit_app,
            width=100
        )

        self.undo_btn.pack(side="left", padx=5)
        self.redo_btn.pack(side="left", padx=5)
        clear_btn.pack(side="left", padx=5)
        exit_btn.pack(side="right", padx=5)

        status_title = ctk.CTkLabel(
            right,
            text="Editor Statistics",
            font=("Segoe UI", 20, "bold")
        )
        status_title.pack(pady=(15, 10))

        self.words = ctk.CTkLabel(right, text="Words : 0", font=("Segoe UI", 15))
        self.words.pack(pady=4)

        self.characters = ctk.CTkLabel(right, text="Characters : 0", font=("Segoe UI", 15))
        self.characters.pack(pady=4)

        self.stack_size = ctk.CTkLabel(right, text="Undo Stack : 1", font=("Segoe UI", 15))
        self.stack_size.pack(pady=4)

        history = ctk.CTkLabel(
            right,
            text="Undo History (Top = Current)",
            font=("Segoe UI", 18, "bold")
        )
        history.pack(pady=(25, 5))

        self.stack_box = ctk.CTkTextbox(
            right,
            font=("Consolas", 12),
            fg_color="#1E1E24"
        )
        self.stack_box.pack(fill="both", expand=True, padx=15, pady=15)

        self.root.bind("<Control-z>", lambda e: self.undo())
        self.root.bind("<Control-y>", lambda e: self.redo())

        self.refresh_ui_elements()

    def handle_key_release(self, event):
        self.update_live_stats()
        current_text = self.textbox.get("1.0", "end-1c")

        if current_text == self.undo_stack[-1]:
            return

        if event.keysym in ("space", "Return", "BackSpace"):
            self.push_new_state(current_text)
        else:
            if self.debounce_timer:
                self.root.after_cancel(self.debounce_timer)
            self.debounce_timer = self.root.after(1000, lambda: self.push_new_state(current_text))

    def push_new_state(self, text_state):
        if self.undo_stack and text_state == self.undo_stack[-1]:
            return
        self.undo_stack.append(text_state)
        self.redo_stack.clear()
        self.refresh_ui_elements()

    def undo(self):
        if len(self.undo_stack) <= 1:
            messagebox.showinfo("Undo", "Nothing left to Undo!")
            return

        popped_state = self.undo_stack.pop()
        self.redo_stack.append(popped_state)

        previous_state = self.undo_stack[-1]
        self.update_textbox_content(previous_state)
        self.refresh_ui_elements()

    def redo(self):
        if not self.redo_stack:
            messagebox.showinfo("Redo", "Nothing to Redo!")
            return

        next_state = self.redo_stack.pop()
        self.undo_stack.append(next_state)

        self.update_textbox_content(next_state)
        self.refresh_ui_elements()

    def clear_text(self):
        if messagebox.askyesno("Confirm", "Clear entire editor?"):
            self.update_textbox_content("")
            self.push_new_state("")

    def update_textbox_content(self, content):
        self.textbox.delete("1.0", "end")
        self.textbox.insert("1.0", content)
        self.update_live_stats()

    def refresh_ui_elements(self):
        self.stack_box.configure(state="normal")
        self.stack_box.delete("1.0", "end")

        for idx, state in enumerate(reversed(self.undo_stack)):
            pos = len(self.undo_stack) - idx
            preview = state.replace("\n", " ").strip()

            if not preview:
                preview = "[Empty State]"
            elif len(preview) > 25:
                preview = preview[:25] + "..."

            marker = " 👉" if idx == 0 else ""
            self.stack_box.insert("end", f"[{pos}]{marker} {preview}\n")

        self.stack_box.configure(state="disabled")
        self.stack_size.configure(text=f"Undo Stack : {len(self.undo_stack)}")

        self.undo_btn.configure(state="normal" if len(self.undo_stack) > 1 else "disabled")
        self.redo_btn.configure(state="normal" if self.redo_stack else "disabled")

    def update_live_stats(self):
        text = self.textbox.get("1.0", "end-1c")
        chars = len(text)
        words = len(text.split())
        self.words.configure(text=f"Words : {words}")
        self.characters.configure(text=f"Characters : {chars}")

    def exit_app(self):
        if messagebox.askyesno("Exit", "Exit application?"):
            self.root.destroy()


if __name__ == "__main__":
    root = ctk.CTk()
    app = TextEditor(root)
    root.mainloop()
