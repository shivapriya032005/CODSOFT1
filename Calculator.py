import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x650")
        self.root.config(bg="#fdf1db")
        self.root.resizable(False, False)

        # Current value and operator
        self.val = 0
        self.opt = ""
        self.new_num = True

        # Define pastel colors for buttons
        self.colors = {
            "bg": "#fdf1db",  # Light pastel background
            "num": "#e4d1ff",  # Pastel purple
            "ops": "#fce2ce",  # Light peach
            "func": "#c9e4de",  # Mint green
            "text": "#606c76"  # Dark gray for text
        }

        # Display Entry
        self.display = tk.Entry(root, width=16, font=("Arial", 28), bd=0, justify="right", relief="flat", bg="#fff9f0")
        self.display.insert(0, "0")
        self.display.place(x=20, y=50, width=360, height=70)

        # Button properties in a list of tuples (text, x, y, command, color)
        buttons = [
            ("AC", 20, 150, self.clear, self.colors["func"]),
            ("C", 110, 150, self.backspace, self.colors["func"]),
            ("%", 200, 150, lambda: self.operation('%'), self.colors["ops"]),
            ("/", 290, 150, lambda: self.operation('/'), self.colors["ops"]),
            ("7", 20, 250, lambda: self.append("7"), self.colors["num"]),
            ("8", 110, 250, lambda: self.append("8"), self.colors["num"]),
            ("9", 200, 250, lambda: self.append("9"), self.colors["num"]),
            ("*", 290, 250, lambda: self.operation('*'), self.colors["ops"]),
            ("4", 20, 350, lambda: self.append("4"), self.colors["num"]),
            ("5", 110, 350, lambda: self.append("5"), self.colors["num"]),
            ("6", 200, 350, lambda: self.append("6"), self.colors["num"]),
            ("-", 290, 350, lambda: self.operation('-'), self.colors["ops"]),
            ("1", 20, 450, lambda: self.append("1"), self.colors["num"]),
            ("2", 110, 450, lambda: self.append("2"), self.colors["num"]),
            ("3", 200, 450, lambda: self.append("3"), self.colors["num"]),
            ("+", 290, 450, lambda: self.operation('+'), self.colors["ops"]),
            ("0", 110, 550, lambda: self.append("0"), self.colors["num"]),
            (".", 20, 550, self.append_point, self.colors["num"]),
            ("=", 200, 550, self.calculate, self.colors["ops"])
        ]

        # Create buttons dynamically
        for (text, x, y, command, color) in buttons:
            self.create_button(text, x, y, command, color)

    def create_button(self, text, x, y, command, color):
        """Create calculator buttons dynamically"""
        button = tk.Button(self.root, text=text, font=("Arial", 24), bg=color, fg=self.colors["text"], command=command, bd=0)
        button.place(x=x, y=y, width=80, height=80)

    def clear(self):
        """Clear the display and reset the calculator"""
        self.display.delete(0, tk.END)
        self.display.insert(0, "0")
        self.val = 0
        self.opt = ""
        self.new_num = True

    def backspace(self):
        """Remove the last digit from the display"""
        current = self.display.get()
        if len(current) > 1:
            self.display.delete(len(current) - 1, tk.END)
        else:
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")

    def append(self, num):
        """Append digits to the display"""
        if self.new_num:
            self.display.delete(0, tk.END)
            self.new_num = False
        current = self.display.get()
        if current == "0":
            self.display.delete(0, tk.END)
        self.display.insert(tk.END, num)

    def append_point(self):
        """Append a decimal point if it doesn't already exist"""
        if "." not in self.display.get():
            self.display.insert(tk.END, ".")

    def operation(self, op):
        """Store the current number and the operator"""
        if self.opt:
            self.calculate()  # Perform previous operation if an operator is chained
        self.val = float(self.display.get())
        self.opt = op
        self.new_num = True

    def calculate(self):
        """Perform the calculation based on the operator"""
        try:
            current_val = float(self.display.get())
            if self.opt == "+":
                self.val += current_val
            elif self.opt == "-":
                self.val -= current_val
            elif self.opt == "*":
                self.val *= current_val
            elif self.opt == "/":
                if current_val != 0:
                    self.val /= current_val
                else:
                    messagebox.showerror("Error", "Cannot divide by zero")
                    return
            elif self.opt == "%":
                self.val = self.val % current_val
            self.display.delete(0, tk.END)
            self.display.insert(0, str(self.val))
            self.opt = ""
            self.new_num = True
        except ValueError:
            messagebox.showerror("Error", "Invalid input")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
