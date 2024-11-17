# Importing tkinter module
from tkinter import *
# Importing calendar module
import calendar

# Function to show the calendar of the given year
def showCalendar():
    # Create a new window to display the calendar
    gui = Tk()
    gui.config(background='grey')
    gui.title("Calendar for the Year")
    gui.geometry("600x700")

    # Get the year from the input field
    try:
        year = int(year_field.get())
        # Generate the calendar for the given year
        gui_content = calendar.calendar(year)
        # Display the calendar
        calYear = Label(gui, text=gui_content, font="consolas 10 bold", justify=LEFT)
        calYear.pack(padx=20, pady=20)
    except ValueError:
        # Handle invalid input
        error_label = Label(gui, text="Please enter a valid year.", font="consolas 12 bold", fg="red")
        error_label.pack(pady=10)

    gui.mainloop()

# Main window for the user input
root = Tk()
root.config(background='light blue')
root.title("Year Calendar")
root.geometry("300x200")

# Label and input field
year_label = Label(root, text="Enter Year:", font="consolas 12 bold", bg='light blue')
year_label.grid(row=1, column=1, padx=20, pady=10)

year_field = Entry(root, font="consolas 12")
year_field.grid(row=1, column=2, padx=20, pady=10)

# Button to show the calendar
show_button = Button(root, text="Show Calendar", command=showCalendar, font="consolas 12 bold", bg='green', fg='white')
show_button.grid(row=2, column=1, columnspan=2, pady=20)

# Run the main loop
root.mainloop()
