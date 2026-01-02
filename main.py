import tkinter as tk
from ui.calculator_ui import CalculatorUI

root = tk.Tk()
root.withdraw()  # hide root window

CalculatorUI(root)

root.mainloop()
