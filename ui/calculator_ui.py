import tkinter as tk
from logic.calculator_logic import evaluate_expression
from theme.dark_theme import *

class CalculatorUI:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Scientific Calculator")
        self.window.geometry("350x450")
        self.window.configure(bg=BG_COLOR)
        self.window.resizable(False, False)

        self.expression = tk.StringVar()

        entry = tk.Entry(
            self.window,
            textvariable=self.expression,
            font=("Arial", 18),
            justify="right",
            bg=FRAME_COLOR,
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR
        )
        entry.pack(fill="x", padx=10, pady=10)

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', 'C', '+'),
            ('=',)
        ]

        for row in buttons:
            frame = tk.Frame(self.window, bg=BG_COLOR)
            frame.pack(expand=True, fill="both")
            for btn in row:
                self._create_button(frame, btn)

    def _create_button(self, frame, value):
        if value == 'C':
            action = lambda: self.expression.set("")
        elif value == '=':
            action = lambda: self.expression.set(
                evaluate_expression(self.expression.get())
            )
        else:
            action = lambda v=value: self.expression.set(
                self.expression.get() + v
            )

        tk.Button(
            frame,
            text=value,
            font=FONT_NORMAL,
            bg=BTN_COLOR,
            fg=TEXT_COLOR,
            activebackground=ACCENT_COLOR,
            command=action
        ).pack(side="left", expand=True, fill="both", padx=2, pady=2)
