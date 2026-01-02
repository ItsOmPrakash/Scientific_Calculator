import tkinter as tk
from ui.home import HomeUI

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("500x500")
root.resizable(False, False)

HomeUI(root)

root.mainloop()
