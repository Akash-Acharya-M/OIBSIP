import tkinter as tk
from tkinter import messagebox
import random
import string
import json
import os

# Function to generate a random password
def generate_password(length):
    # Ensure there's at least one of each required character type
    if length < 4:  # Minimum length to satisfy the requirements
        messagebox.showerror("Input Error", "Password length must be at least 4.")
        return None

    # Character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special_characters = "!$."

    # Start the password with one of each required character
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random choices from all character types
    all_characters = lower + upper + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the created password list to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

# Function to save password with a tag
def save_password():
    password = password_entry.get()
    tag = tag_entry.get()
    
    if password and tag:
        # Load existing history or initialize an empty list
        if os.path.exists('password_history.json'):
            with open('password_history.json', 'r') as file:
                history = json.load(file)
        else:
            history = []

        # Append new password with tag to history
        history.append({"tag": tag, "password": password})

        # Save updated history back to file
        with open('password_history.json', 'w') as file:
            json.dump(history, file)

        # Clear entries and show success message
        password_entry.delete(0, tk.END)
        tag_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Password saved successfully.")
    else:
        messagebox.showerror("Input Error", "Please enter both a password and a tag.")

# Function to generate and display a password
def display_password():
    length = length_entry.get()
    try:
        length = int(length)
        password = generate_password(length)
        if password:  # Only insert if password generation was successful
            password_entry.delete(0, tk.END)  # Clear previous entry
            password_entry.insert(0, password)  # Insert new password
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid length.")

# Function to load and display password history
def load_history():
    history_window = tk.Toplevel(app)
    history_window.title("Password History")

    # Load existing history
    if os.path.exists('password_history.json'):
        with open('password_history.json', 'r') as file:
            history = json.load(file)

        # Create a text widget to display history
        history_text = tk.Text(history_window, width=50, height=15)
        history_text.pack(padx=10, pady=10)

        # Insert history into the text widget
        for entry in history:
            history_text.insert(tk.END, f"Tag: {entry['tag']}, Password: {entry['password']}\n")
    else:
        messagebox.showinfo("History", "No password history found.")

# Create the main application window
app = tk.Tk()
app.title("Password Generator")

# Set the window size
app.geometry("400x400")

# Create a label and entry for password length
length_label = tk.Label(app, text="Password Length (min 4):")
length_label.pack(pady=10)
length_entry = tk.Entry(app)
length_entry.pack(pady=5)

# Create a button to generate password
generate_button = tk.Button(app, text="Generate Password", command=display_password, bg="#4CAF50", fg="white", padx=10, pady=5)
generate_button.pack(pady=10)

# Create a label and entry for generated password
password_label = tk.Label(app, text="Generated Password:")
password_label.pack(pady=10)
password_entry = tk.Entry(app, width=40)
password_entry.pack(pady=5)

# Create a label and entry for tag
tag_label = tk.Label(app, text="Tag:")
tag_label.pack(pady=10)
tag_entry = tk.Entry(app)
tag_entry.pack(pady=5)

# Create a button to save password
save_button = tk.Button(app, text="Save Password", command=save_password, bg="#2196F3", fg="white", padx=10, pady=5)
save_button.pack(pady=10)

# Create a button to load history
history_button = tk.Button(app, text="View Password History", command=load_history, bg="#FF9800", fg="white", padx=10, pady=5)
history_button.pack(pady=10)

# Start the GUI event loop
app.mainloop()
