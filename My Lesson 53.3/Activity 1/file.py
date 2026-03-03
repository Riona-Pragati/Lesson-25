import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x250")
root.resizable(False, False)

title_label = tk.Label(root, text="Random Password Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

length_frame = tk.Frame(root)
length_frame.pack(pady=5)

length_label = tk.Label(length_frame, text="Password Length:")
length_label.pack(side=tk.LEFT)

length_entry = tk.Entry(length_frame, width=5)
length_entry.insert(0, "12")
length_entry.pack(side=tk.LEFT)

password_entry = tk.Entry(root, width=40, font=("Arial", 12))
password_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

generate_button = tk.Button(button_frame, text="Generate Password", command=generate_password)
generate_button.pack(side=tk.LEFT, padx=5)

copy_button = tk.Button(button_frame, text="Copy", command=copy_password)
copy_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
