#!/usr/bin/env python3

import cv2
import numpy as np
import sys

symbols_list = ["#", "-", "*", ".", "+", "o"]
threshold_list = [0, 50, 100, 150, 200]


def print_out_ascii(array):
    """Prints the coded image with symbols."""
    for row in array:
        for e in row:
            # Select symbol based on the intensity
            print(symbols_list[int(e) % len(symbols_list)], end="")
        print()


def img_to_ascii(image):
    """Returns the numeric code image."""
    # Get image dimensions
    height, width = image.shape
    new_width = int(width / 20)
    new_height = int(height / 40)

    # Resize image to fit the screen
    resized_image = cv2.resize(image, (new_width, new_height))

    # Create an array for thresholded image
    thresh_image = np.zeros(resized_image.shape, dtype=np.uint8)

    # Assign values based on thresholds
    for i, threshold in enumerate(threshold_list):
        thresh_image[resized_image > threshold] = i

    return thresh_image


if __name__ == "__main__":
    # Check if an image path was provided
    if len(sys.argv) < 2:
        print("Image path not specified: Using sample_image.png\n")
        image_path = "sample_image.png"  # Default image path
    else:
        image_path = sys.argv[1]

    # Read the image in grayscale
    image = cv2.imread(image_path, 0)

    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Could not read the image at {image_path}. Please check the file path.")
        sys.exit()

    # Convert the image to ASCII art
    ascii_art = img_to_ascii(image)

    # Print the ASCII art
    print_out_ascii(ascii_art)
