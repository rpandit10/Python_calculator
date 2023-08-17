import tkinter as tk


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.create_widgets()

    def create_widgets(self):
        # Result display
        result_label = tk.Label(self.root, textvariable=self.result_var, font=("Helvetica", 24), anchor="e")
        result_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="news")

        # Calculator buttons
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Helvetica", 18),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="news")

        # Terminate button
        terminate_button = tk.Button(self.root, text="Terminate", font=("Helvetica", 14), command=self.root.quit)
        terminate_button.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky="news")

    def on_button_click(self, button_text):
        current_text = self.result_var.get()

        if button_text == "=":
            try:
                result = str(eval(current_text))
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        else:
            if current_text == "0" or current_text == "Error":
                self.result_var.set(button_text)
            else:
                self.result_var.set(current_text + button_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
