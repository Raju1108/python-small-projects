import os
import argparse
import pyautogui
import time

# Set up argument parser
parser = argparse.ArgumentParser()

parser.add_argument("-p", "--path", help="Absolute path to store screenshot.", default=r"./images")
parser.add_argument("-t", "--type", help="h (hourly), m (minutes), or s (seconds)", default='h')
parser.add_argument("-f", "--frequency", help="Frequency for taking screenshot per h/m/s.", default=1, type=int)

args = parser.parse_args()

# Convert frequency to seconds
sec = 0.0
if args.type == 'h':
    sec = 60 * 60 / args.frequency
elif args.type == 'm':
    sec = 60 / args.frequency
elif args.type == 's':
    sec = 1 / args.frequency

# Ensure delay is at least 1 second
if sec < 1.0:
    sec = 1.0

# Create the directory if it doesn't exist
if not os.path.exists(args.path):
    os.makedirs(args.path)

try:
    while True:
        # Get the current time
        t = time.localtime()
        current_time = time.strftime("%H_%M_%S", t)
        filename = f"{current_time}.png"
        
        # Capture screenshot and save it to the specified path
        filepath = os.path.join(args.path, filename)
        pyautogui.screenshot(filepath)
        
        print(f"{filename} saved successfully at {filepath}.")
        
        # Wait before the next screenshot
        time.sleep(sec)

except KeyboardInterrupt:
    print("Script terminated by user.")
