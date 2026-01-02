import tkinter as tk

def open_calculator():
    print("Calculator clicked")

def open_bmi():
    print("BMI clicked")

def open_converter():
    print("Converter clicked")

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("500x500")
root.resizable(False, False)

tk.Label(
    root,
    text="Scientific Calculator",
    font=("Arial", 20, "bold")
).pack(pady=30)

tk.Button(root, text="Scientific Calculator", width=30, height=2, command=open_calculator).pack(pady=10)
tk.Button(root, text="BMI Calculator", width=30, height=2, command=open_bmi).pack(pady=10)
tk.Button(root, text="Unit Converters", width=30, height=2, command=open_converter).pack(pady=10)

root.mainloop()
