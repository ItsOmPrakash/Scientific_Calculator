import tkinter as tk

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("500x500")
root.resizable(False, False)

label = tk.Label(root, text="Scientific Calculator", font=("Arial", 20))
label.pack(pady=20)

root.mainloop()
