import tkinter as tk
from tkinter import messagebox

class CandyDispenserApp:
    def __init__(self, root):
        self.stack = []  # Initialize the stack
        self.max_capacity = 9  # Maximum candies the stack can hold
        self.root = root
        self.root.title("Candy Dispenser")

        # Title Label
        self.title_label = tk.Label(root, text="Candy Dispenser", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Canvas for Stack Visualization
        self.canvas = tk.Canvas(root, width=200, height=300, bg="white", highlightthickness=1, highlightbackground="black")
        self.canvas.pack(pady=10)

        # Input for Candy Name
        self.entry_label = tk.Label(root, text="Enter Candy Name:")
        self.entry_label.pack(pady=5)
        self.entry = tk.Entry(root, width=25)
        self.entry.pack(pady=5)

        # Buttons for Stack Operations
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.push_button = tk.Button(self.button_frame, text="Push", command=self.push)
        self.push_button.grid(row=0, column=0, padx=5)

        self.pop_button = tk.Button(self.button_frame, text="Pop", command=self.pop)
        self.pop_button.grid(row=0, column=1, padx=5)

        self.top_button = tk.Button(self.button_frame, text="Top", command=self.get_top)
        self.top_button.grid(row=0, column=2, padx=5)

        self.is_empty_button = tk.Button(self.button_frame, text="Is Empty", command=self.is_empty)
        self.is_empty_button.grid(row=1, column=0, padx=5, pady=5)

        self.is_full_button = tk.Button(self.button_frame, text="Is Full", command=self.is_full)
        self.is_full_button.grid(row=1, column=1, padx=5, pady=5)

        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=1, column=2, padx=5, pady=5)

    def draw_stack(self):
        # Draws the stack as ovals in a container, starting from the bottom
        self.canvas.delete("all")
        container_margin = 10
        candy_height = 30
        candy_width = 150
        container_height = 280
        container_width = 180

        # Draw the container
        self.canvas.create_rectangle(
            container_margin,
            container_margin,
            container_width + container_margin,
            container_height + container_margin,
            outline="black",
            width=2,
        )

        # Draw candies from bottom to top of the stack
        for i, candy in enumerate(self.stack):
            y_offset = container_height - (i + 1) * candy_height
            x_start = (container_width - candy_width) // 2 + container_margin
            x_end = x_start + candy_width
            y_start = y_offset
            y_end = y_offset + candy_height

            self.canvas.create_oval(
                x_start, y_start, x_end, y_end, fill="lightblue", outline="blue"
            )
            self.canvas.create_text(
                (x_start + x_end) // 2,
                (y_start + y_end) // 2,
                text=candy,
                font=("Arial", 10),
                fill="black",
            )

    def push(self):
        # Pushes a candy onto the stack
        candy = self.entry.get().strip()
        if candy:
            if len(self.stack) >= self.max_capacity:
                messagebox.showwarning("Stack Overflow", "The container is full!")
            else:
                self.stack.append(candy)
                self.draw_stack()
                self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a candy name!")

    def pop(self):
        # Pops the top candy from the stack
        if self.stack:
            popped_candy = self.stack.pop()
            self.draw_stack()
            messagebox.showinfo("Pop Operation", f"Popped candy: {popped_candy}")
        else:
            messagebox.showwarning("Stack Empty", "No candies to pop!")

    def get_top(self):
        # Gets the top candy from the stack
        if self.stack:
            top_candy = self.stack[-1]
            messagebox.showinfo("Top Candy", f"Top candy: {top_candy}")
        else:
            messagebox.showwarning("Stack Empty", "No candies in the stack!")

    def is_empty(self):
        """Checks if the stack is empty."""
        messagebox.showinfo("Is Empty", "Stack is empty!" if not self.stack else "Stack is not empty.")

    def is_full(self):
        # Checks if the stack is full
        messagebox.showinfo("Is Full", "Stack is full!" if len(self.stack) >= self.max_capacity else "Stack is not full.")

    def reset(self):
        # Resets the stack.
        self.stack = []
        self.draw_stack()
        messagebox.showinfo("Reset", "Candy dispenser has been reset!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CandyDispenserApp(root)
    root.mainloop()
