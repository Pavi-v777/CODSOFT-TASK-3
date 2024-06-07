import random
import string
import tkinter as tk
from tkinter import messagebox, Entry, Button


# Function to generate a password
def generate_password():
    length = int(length_entry.get())

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def accept_password():
    password_entry.focus()
    messagebox.askquestion("Accept", "Are you sure want to accept?")
def rest_password():
    password_entry.delete(0, tk.END)
    (messagebox.showinfo("Reset","Enter new password length again"))
    password_entry.insert(0, password_entry.get())
    password_entry.focus()

# Set up the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.configure(background="black")
# Add widgets to the window
length_label = tk.Label(root, text="Password Length:",font=('Arial', 10, 'bold'))
length_label.pack(pady=10)

length_entry=tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", bg="blue", fg="white", command=generate_password,font=('Arial', 10, 'bold'))
generate_button.pack(pady=20)

password_label = tk.Label(root, text="Generated Password:",font=('Arial', 10, 'bold'))
password_label.pack(pady=10)

password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=5)

accept_button = tk.Button(root, text="Accept", bg="blue", fg="white",font=('Arial', 10, 'bold'),command=accept_password)
accept_button.pack(pady=20)

reset_button = tk.Button(root, text="Reset",bg="blue", fg="white",command=rest_password,font=('Arial', 10, 'bold'))
reset_button.pack(pady=5)
# Run the application
root.mainloop()