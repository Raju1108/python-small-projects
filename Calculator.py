from tkinter import *

# Main function to run the calculator
def love():
    class Calculator:
        def __init__(self, master):
            self.master = master
            master.title("Python Calculator")
            master.configure(bg='#cb464e')

            # Create screen widget
            self.screen = Text(
                master, state='disabled', width=60, height=3,
                background="#fcfcec", foreground="#cb464e",
                font=("times", 12, "bold")
            )
            self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
            self.screen.configure(state='normal')

            # Initialize equation as an empty string
            self.equation = ''

            # Create buttons
            buttons = [
                self.createButton(7), self.createButton(8), self.createButton(9), self.createButton(u"\u232B", None),
                self.createButton(4), self.createButton(5), self.createButton(6), self.createButton(u"\u00F7"),
                self.createButton(1), self.createButton(2), self.createButton(3), self.createButton('*'),
                self.createButton('.'), self.createButton(0), self.createButton('+'), self.createButton('-'),
                self.createButton('=', None, 34)
            ]

            # Arrange buttons with grid manager
            count = 0
            for row in range(1, 5):
                for column in range(4):
                    buttons[count].grid(row=row, column=column)
                    count += 1

            # Place the '=' button at the bottom
            buttons[16].grid(row=5, column=0, columnspan=4)

        # Method to create a button
        def createButton(self, val, write=True, width=7):
            return Button(
                self.master, text=val, command=lambda: self.click(val, write),
                width=width, background='#4b7fa4', foreground="#fcfcec",
                font=("times", 20)
            )

        # Method to handle button click
        def click(self, text, write):
            if write is None:
                # Evaluate the equation if '=' is clicked
                if text == '=' and self.equation:
                    try:
                        # Evaluate the equation
                        self.equation = self.equation.replace(u"\u00F7", "/")
                        answer = str(eval(self.equation))
                        self.clear_screen()
                        self.insert_screen(answer, newline=True)
                    except Exception as e:
                        self.clear_screen()
                        self.insert_screen("Error", newline=True)
                elif text == u"\u232B":
                    # Clear screen if 'Backspace' is clicked
                    self.clear_screen()
            else:
                # Insert the clicked button value on the screen
                self.insert_screen(text)

        # Method to clear the screen
        def clear_screen(self):
            self.equation = ''
            self.screen.configure(state='normal')
            self.screen.delete('1.0', END)

        # Method to insert value on the screen
        def insert_screen(self, value, newline=False):
            self.screen.configure(state='normal')
            self.screen.insert(END, value)
            self.equation += str(value)
            self.screen.configure(state='disabled')

    # Create the main window and run the application
    root = Tk()
    Calculator(root)
    root.mainloop()

# Run the calculator
love()
