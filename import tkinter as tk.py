import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("400x500")
        master.config(bg="#FFB6C1")  

        self.result_var = tk.StringVar()

        # Entry field for displaying the result
        self.entry = tk.Entry(master, textvariable=self.result_var, font=('Helvetica', 24), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right', bg="#FFFFFF")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(master, text=button, padx=20, pady=20, font=('Helvetica', 18),
                      command=lambda b=button: self.on_button_click(b), bg="#FFFACD", fg="#000000", activebackground="#FFEFD5").grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Clear button
        tk.Button(master, text='C', padx=20, pady=20, font=('Helvetica', 18), command=self.clear, bg="#FFCCCB", fg="#000000", activebackground="#FFB6C1").grid(row=row_val, column=0, sticky="nsew", padx=5, pady=5)

        # Configure grid weights for responsive design
        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
            master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == '=':
            try:
                expression = self.result_var.get()
                result = eval(expression)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            new_text = current_text + str(char)
            self.result_var.set(new_text)

    def clear(self):
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()