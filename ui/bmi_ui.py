import tkinter as tk
from logic.bmi_logic import calculate_bmi
from theme.dark_theme import *

class BMIUI:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("BMI Calculator")
        self.window.geometry("350x350")
        self.window.configure(bg=BG_COLOR)
        self.window.resizable(False, False)

        tk.Label(
            self.window,
            text="BMI Calculator",
            font=FONT_TITLE,
            bg=BG_COLOR,
            fg=TEXT_COLOR
        ).pack(pady=20)

        self.weight_entry = self.create_entry("Weight (kg)")
        self.height_entry = self.create_entry("Height (m)")

        tk.Button(
            self.window,
            text="Calculate BMI",
            font=FONT_NORMAL,
            bg=BTN_COLOR,
            fg=TEXT_COLOR,
            activebackground=ACCENT_COLOR,
            command=self.calculate
        ).pack(pady=20)

        self.result_label = tk.Label(
            self.window,
            text="",
            font=FONT_NORMAL,
            bg=BG_COLOR,
            fg=TEXT_COLOR
        )
        self.result_label.pack(pady=10)

    def create_entry(self, label_text):
        tk.Label(
            self.window,
            text=label_text,
            bg=BG_COLOR,
            fg=TEXT_COLOR
        ).pack()
        entry = tk.Entry(
            self.window,
            bg=FRAME_COLOR,
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR
        )
        entry.pack(pady=5)
        return entry

    def calculate(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            bmi = calculate_bmi(weight, height)

            if bmi is None:
                self.result_label.config(text="Invalid input")
            else:
                self.result_label.config(text=f"BMI: {bmi}")
        except:
            self.result_label.config(text="Please enter valid numbers")
