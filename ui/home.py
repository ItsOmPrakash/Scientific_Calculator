import tkinter as tk
from theme.dark_theme import *

class HomeUI:
    def __init__(self, root):
        self.root = root
        root.configure(bg=BG_COLOR)

        tk.Label(
            root,
            text="Scientific Calculator",
            font=FONT_TITLE,
            bg=BG_COLOR,
            fg=TEXT_COLOR
        ).pack(pady=30)

        self.create_button("Scientific Calculator", self.open_calculator)
        self.create_button("BMI Calculator", self.open_bmi)
        self.create_button("Unit Converters", self.open_converter)

    def create_button(self, text, command):
        tk.Button(
            self.root,
            text=text,
            font=FONT_NORMAL,
            bg=BTN_COLOR,
            fg=TEXT_COLOR,
            activebackground=ACCENT_COLOR,
            width=30,
            height=2,
            command=command
        ).pack(pady=10)

    def open_calculator(self):
        from ui.calculator_ui import CalculatorUI
        CalculatorUI(self.root)

    def open_bmi(self):
        from ui.bmi_ui import BMIUI
        BMIUI(self.root)

    def open_converter(self):
        from ui.converter_ui import ConverterUI
        ConverterUI(self.root)
