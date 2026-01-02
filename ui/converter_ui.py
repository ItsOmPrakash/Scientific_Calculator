import tkinter as tk
from logic.converter_logic import *
from theme.dark_theme import *

class ConverterUI:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Unit Converter")
        self.window.geometry("400x450")
        self.window.configure(bg=BG_COLOR)
        self.window.resizable(False, False)

        tk.Label(
            self.window,
            text="Unit Converter",
            font=FONT_TITLE,
            bg=BG_COLOR,
            fg=TEXT_COLOR
        ).pack(pady=15)

        self.entry = tk.Entry(
            self.window,
            bg=FRAME_COLOR,
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR
        )
        self.entry.pack(pady=10)

        self.result = tk.Label(
            self.window,
            text="",
            font=FONT_NORMAL,
            bg=BG_COLOR,
            fg=TEXT_COLOR
        )
        self.result.pack(pady=10)

        self.create_button("Meter → CM", lambda: self.convert(meter_to_cm))
        self.create_button("CM → Meter", lambda: self.convert(cm_to_meter))
        self.create_button("Celsius → Fahrenheit", lambda: self.convert(celsius_to_fahrenheit))
        self.create_button("Fahrenheit → Celsius", lambda: self.convert(fahrenheit_to_celsius))
        self.create_button("Km/h → m/s", lambda: self.convert(kmph_to_mps))
        self.create_button("m/s → Km/h", lambda: self.convert(mps_to_kmph))

    def create_button(self, text, command):
        tk.Button(
            self.window,
            text=text,
            font=FONT_NORMAL,
            bg=BTN_COLOR,
            fg=TEXT_COLOR,
            activebackground=ACCENT_COLOR,
            command=command
        ).pack(pady=4)

    def convert(self, func):
        try:
            value = float(self.entry.get())
            result = func(value)
            self.result.config(text=f"Result: {round(result, 3)}")
        except:
            self.result.config(text="Invalid input")
