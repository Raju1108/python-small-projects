'''
Instructions:
1. Install captcha: pip install captcha
2. Ensure the font files are in the specified paths
3. Run the code
'''

from io import BytesIO
from tkinter import *
from random import randint
from tkinter import messagebox
from captcha.image import ImageCaptcha
import os

# Check if the font files exist
if not (os.path.exists(r'C:\Users\rajus\Downloads\ChelseaMarketsr.ttf') and os.path.exists(r'C:\Users\rajus\Downloads\DejaVuSanssr.ttf')):
    print("Font files not found. Please check the paths.")
    exit()

# Initialize ImageCaptcha with custom fonts
image = ImageCaptcha(fonts=[r'C:\Users\rajus\Downloads\ChelseaMarketsr.ttf', r'C:\Users\rajus\Downloads\DejaVuSanssr.ttf'])

# Generate a random 6-digit number
random_code = str(randint(100000, 999999))
data = image.generate(random_code)
image.write(random_code, 'out.png')

def verify():
    global random_code
    user_input = t1.get("1.0", END).strip()
    if user_input == random_code:
        messagebox.showinfo("Success", "Verified")
    else:
        messagebox.showinfo("Alert", "Not Verified")
        refresh()

def refresh():
    global random_code, photo
    random_code = str(randint(100000, 999999))
    data = image.generate(random_code)
    image.write(random_code, 'out.png')
    photo = PhotoImage(file="out.png")
    l1.config(image=photo)
    l1.photo = photo  # Retain reference to avoid garbage collection
    l1.update()

# Main Tkinter window
root = Tk()
root.title("Captcha Verification")
root.geometry("300x300")

# Load the captcha image
photo = PhotoImage(file="out.png")

# Create Tkinter widgets
l1 = Label(root, image=photo, height=100, width=200)
t1 = Text(root, height=1, width=20)
b1 = Button(root, text="Submit", command=verify)
b2 = Button(root, text="Refresh", command=refresh)

# Arrange widgets in the window
l1.pack(pady=10)
t1.pack(pady=10)
b1.pack(pady=5)
b2.pack(pady=5)

# Run the Tkinter main loop
root.mainloop()
