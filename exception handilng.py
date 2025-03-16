import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("400x500")
        master.config(bg="#FFB6C1")  

        self.result_var = tk.StringVar()

        # Entry field for displaying the result
        self.create_display()
        self.create_buttons()
        
    def create_display(self):
        self.entry = tk.Entry(self.master, textvariable=self.result_var, font=('Helvetica', 24),
                              bd=10, insertwidth=2, width=14, borderwidth=4, justify='right', bg="#FFFFFF")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

        # Special buttons: Clear (C) and Backspace (←)
        self.create_button('C', 5, 0, self.clear, "#FFCCCB")
        self.create_button('←', 5, 1, self.backspace, "#D3D3D3")

        # Grid configuration for responsiveness
        for i in range(6):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def create_button(self, text, row, col, command=None, bg="#FFFACD"):
        action = command if command else lambda b=text: self.on_button_click(b)
        tk.Button(self.master, text=text, padx=20, pady=20, font=('Helvetica', 18),
                  command=action, bg=bg, fg="#000000", activebackground="#FFEFD5").grid(
                  row=row, column=col, sticky="nsew", padx=5, pady=5)

    def on_button_click(self, char):
        if char == '=':
            self.calculate()
        else:
            self.result_var.set(self.result_var.get() + str(char))

    def calculate(self):
        try:
            expression = self.result_var.get()
            result = eval(expression)
            self.result_var.set(result)
        except ZeroDivisionError:
            self.result_var.set("Cannot divide by zero")
        except Exception:
            self.result_var.set("Error")

    def clear(self):
        self.result_var.set("")

    def backspace(self):
        self.result_var.set(self.result_var.get()[:-1])

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
