import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        # Get height and weight from user input
        height = float(height_entry.get())  # Height in meters
        weight = float(weight_entry.get())  # Weight in kilograms
        
        # Calculate BMI
        bmi = weight / (height ** 2)
        
        # Format the result to two decimal places
        bmi_result = f"Your BMI is: {bmi:.2f}"
        
        # Display the result in a message box
        messagebox.showinfo("BMI Result", bmi_result)
    except ValueError:
        # Handle any value errors (e.g., non-numeric input)
        messagebox.showerror("Input Error", "Please enter valid numbers for height and weight.")

# Create the main application window
app = tk.Tk()
app.title("BMI Calculator")

# Set the window size
app.geometry("300x200")

# Create a label for height
height_label = tk.Label(app, text="Height (m):")
height_label.pack(pady=10)

# Create an entry widget for height input
height_entry = tk.Entry(app)
height_entry.pack(pady=5)

# Create a label for weight
weight_label = tk.Label(app, text="Weight (kg):")
weight_label.pack(pady=10)

# Create an entry widget for weight input
weight_entry = tk.Entry(app)
weight_entry.pack(pady=5)

# Create a button to calculate BMI
calculate_button = tk.Button(app, text="Calculate BMI", command=calculate_bmi, relief="flat", bg="#4CAF50", fg="white", padx=10, pady=5)
calculate_button.pack(pady=20)

# Style the button to have rounded corners
calculate_button.config(borderwidth=0)
calculate_button.bind("<Enter>", lambda e: calculate_button.config(bg="#45a049"))
calculate_button.bind("<Leave>", lambda e: calculate_button.config(bg="#4CAF50"))

# Start the GUI event loop
app.mainloop()
