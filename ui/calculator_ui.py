import tkinter as tk
import math

from theme.dark_theme import *
from logic.calculator_logic import (
    evaluate_expression,
    sin,
    cos,
    tan,
    sqrt,
    log
)

from ui.bmi_ui import BMIUI
from ui.converter_ui import ConverterUI


class CalculatorUI:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Scientific Calculator")
        self.window.geometry("380x550")
        self.window.configure(bg=BG_COLOR)
        self.window.resizable(False, False)

        self.expression = tk.StringVar()

        # ================= Display =================
        entry = tk.Entry(
            self.window,
            textvariable=self.expression,
            font=("Arial", 20),
            justify="right",
            bg=FRAME_COLOR,
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            relief="flat"
        )
        entry.pack(fill="x", padx=10, pady=15)

        # ================= Buttons Layout =================
        buttons = [
            ('sin', 'cos', 'tan', '√'),
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', 'π', '+'),
            ('C', '=',)
        ]

        for row in buttons:
            frame = tk.Frame(self.window, bg=BG_COLOR)
            frame.pack(expand=True, fill="both", padx=5)
            for btn in row:
                self.create_button(frame, btn)

        # ================= More Options =================
        tk.Button(
            self.window,
            text="More Options",
            font=FONT_NORMAL,
            bg=ACCENT_COLOR,
            fg="white",
            activebackground=BTN_COLOR,
            relief="flat",
            command=self.open_more_options
        ).pack(fill="x", padx=10, pady=10)

    # =====================================================
    # Button Creation Logic
    # =====================================================
    def create_button(self, frame, value):

        if value == 'C':
            action = lambda: self.expression.set("")

        elif value == '=':
            action = lambda: self.expression.set(
                evaluate_expression(self.expression.get())
            )

        elif value == 'sin':
            action = lambda: self.apply_function(sin)

        elif value == 'cos':
            action = lambda: self.apply_function(cos)

        elif value == 'tan':
            action = lambda: self.apply_function(tan)

        elif value == '√':
            action = lambda: self.apply_function(sqrt)

        elif value == 'π':
            action = lambda: self.expression.set(
                self.expression.get() + "π"
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
            relief="flat",
            command=action
        ).pack(side="left", expand=True, fill="both", padx=3, pady=3)

    # =====================================================
    # Apply Scientific Function
    # =====================================================
    def apply_function(self, func):
        try:
            value = float(self.expression.get())
            self.expression.set(str(func(value)))
        except:
            self.expression.set("Error")

    # =====================================================
    # More Options Window
    # =====================================================
    def open_more_options(self):
        win = tk.Toplevel(self.window)
        win.title("More Options")
        win.geometry("300x220")
        win.configure(bg=BG_COLOR)
        win.resizable(False, False)

        tk.Label(
            win,
            text="More Options",
            font=FONT_TITLE,
            bg=BG_COLOR,
            fg=TEXT_COLOR
        ).pack(pady=20)

        tk.Button(
            win,
            text="BMI Calculator",
            font=FONT_NORMAL,
            bg=BTN_COLOR,
            fg=TEXT_COLOR,
            activebackground=ACCENT_COLOR,
            relief="flat",
            command=lambda: BMIUI(self.window)
        ).pack(fill="x", padx=20, pady=8)

        tk.Button(
            win,
            text="Unit Converter",
            font=FONT_NORMAL,
            bg=BTN_COLOR,
            fg=TEXT_COLOR,
            activebackground=ACCENT_COLOR,
            relief="flat",
            command=lambda: ConverterUI(self.window)
        ).pack(fill="x", padx=20, pady=8)
