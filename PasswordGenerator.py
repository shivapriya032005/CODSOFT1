import tkinter as tk
from tkinter import messagebox
import random
import string

# Improved Code

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4 to include all selected types!")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length!")
        return

    character_pool = ''
    guaranteed_chars = []

    if upper_case_var.get():
        character_pool += string.ascii_uppercase
        guaranteed_chars.append(random.choice(string.ascii_uppercase))
    if lower_case_var.get():
        character_pool += string.ascii_lowercase
        guaranteed_chars.append(random.choice(string.ascii_lowercase))
    if number_var.get():
        character_pool += string.digits
        guaranteed_chars.append(random.choice(string.digits))
    if symbol_var.get():
        character_pool += string.punctuation
        guaranteed_chars.append(random.choice(string.punctuation))

    if not character_pool:
        messagebox.showerror("Error", "At least one character type must be selected!")
        return

    remaining_length = length - len(guaranteed_chars)

    if remaining_length < 0:
        messagebox.showerror("Error", "Password length is too short to include all selected types!")
        return

    # Fill the remaining password length with random characters from the pool
    password = guaranteed_chars + [random.choice(character_pool) for _ in range(remaining_length)]

    # Shuffle the password to randomize character positions
    random.shuffle(password)
    final_password = ''.join(password)

    result_var.set(final_password)
    update_result()

def update_result():
    result_textbox.config(state=tk.NORMAL)
    result_textbox.delete(1.0, tk.END)
    result_textbox.insert(tk.END, result_var.get())
    result_textbox.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x550")
root.configure(bg="#FFFFFF")  # Light background

# Custom Font
font = ("Roboto", 12)  # Example font

# Title Label Frame
title_frame = tk.Frame(root, bg="#FFFFFF")
title_label = tk.Label(title_frame, text="Password Generator", font=(font[0], 16, "bold"), bg="#FFFFFF", fg="#303F9F")
title_label.pack(pady=20)
title_frame.pack(pady=10)

# Input and Checkbox Frame
input_frame = tk.Frame(root, bg="#FFFFFF")

tk.Label(input_frame, text="Password Length:", bg="#FFFFFF", font=font).pack(pady=5)
length_entry = tk.Entry(input_frame, font=font, width=5)
length_entry.pack(pady=5)

upper_case_var = tk.BooleanVar()
lower_case_var = tk.BooleanVar()
number_var = tk.BooleanVar()
symbol_var = tk.BooleanVar()

tk.Checkbutton(input_frame, text="Include Uppercase Letters", variable=upper_case_var, bg="#FFFFFF", font=font).pack(pady=5)
tk.Checkbutton(input_frame, text="Include Lowercase Letters", variable=lower_case_var, bg="#FFFFFF", font=font).pack(pady=5)
tk.Checkbutton(input_frame, text="Include Numbers", variable=number_var, bg="#FFFFFF", font=font).pack(pady=5)
tk.Checkbutton(input_frame, text="Include Symbols", variable=symbol_var, bg="#FFFFFF", font=font).pack(pady=5)

input_frame.pack(pady=10)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#4285F4", fg="white", font=(font[0], 12, "bold"))
generate_button.pack(pady=20)

# Result Display Frame
result_frame = tk.Frame(root)

result_var = tk.StringVar()
result_label = tk.Label(result_frame, text="Generated Password:", bg="#FFFFFF", font=(font[0], 12, "bold"))
result_label.pack(pady=5)

result_textbox = tk.Text(result_frame, height=2, width=40, font=font, bg="#F0F0F0", wrap=tk.WORD, borderwidth=1, relief="groove")
result_textbox.pack(pady=5)
result_textbox.config(state=tk.DISABLED)

result_frame.pack()

# Start the loop
root.mainloop()