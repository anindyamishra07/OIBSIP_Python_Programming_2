import tkinter as tk
from tkinter import messagebox

def calc_bmi():
    try:
        weight = float(weight_input.get())
        height = float(height_input.get()) / 100
        bmi = weight / (height ** 2)
        
        if bmi < 18.5:
            your_category = "You are Underweight"
        elif 18.5 <= bmi < 24.9:
            your_category = "You are Normal weight"
        elif 25 <= bmi < 29.9:
            your_category = "You are Overweight"
        else:
            your_category = "You are Obese"
        
        messagebox.showinfo(" The BMI Result", f"BMI is {bmi:.2f} ({your_category})")
    
    except ValueError:
        messagebox.showerror("Error", "Please enter valid details.")

root = tk.Tk()
root.title(" The BMI Calculator")
root.geometry("500x250")
root.resizable(False, False)

tk.Label(root, text="Weight (kg):").pack(pady=5)
weight_input = tk.Entry(root)
weight_input.pack()

tk.Label(root, text="Height (cm):").pack(pady=5)
height_input = tk.Entry(root)
height_input.pack()

calc_button = tk.Button(root, text="Calculate your BMI", command=calc_bmi)
calc_button.pack(pady=10)

root.mainloop()