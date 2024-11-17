import os
import shutil
import sys
import cv2
import time
import argparse
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

class FrameCapture:
    '''
    Class definition to capture frames
    '''
    def __init__(self, file_path, output_directory="captured_frames"):
        '''
        Initializing directory where the captured frames will be stored
        '''
        self.directory = output_directory
        self.file_path = file_path
        if os.path.exists(self.directory):
            print(f"Warning: Directory '{self.directory}' already exists. Frames will be overwritten.")
            shutil.rmtree(self.directory)  # Remove existing directory
        os.mkdir(self.directory)

    def save_frame(self, frame_number, image):
        '''
        Saves a single frame to the disk.
        '''
        capture = os.path.join(self.directory, f'frame{frame_number:04d}.jpg')
        cv2.imwrite(capture, image)
        print(f"Captured {capture}")

    def capture_frames(self, frame_interval=1):
        '''
        This method captures frames from the video file provided
        '''
        cv2_object = cv2.VideoCapture(self.file_path)
        if not cv2_object.isOpened():
            print(f"Error: Unable to open video file '{self.file_path}'.")
            sys.exit(1)

        total_frames = int(cv2_object.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_number = 0
        frames_captured = 0

        # Using a progress bar to show the capture progress
        with tqdm(total=total_frames, desc="Capturing frames", unit="frame") as pbar:
            with ThreadPoolExecutor(max_workers=4) as executor:  # Adjust max_workers as needed
                while True:
                    frame_found, image = cv2_object.read()
                    if not frame_found or image is None:
                        break  # Exit loop if no frame is found (end of video)

                    # Capture frames at specific intervals
                    if frame_number % frame_interval == 0:
                        executor.submit(self.save_frame, frame_number, image)  # Process frame in parallel
                        frames_captured += 1

                    frame_number += 1
                    pbar.update(1)  # Update progress bar

        cv2_object.release()
        print(f"Finished capturing frames. Total frames captured: {frames_captured}")

def parse_arguments():
    '''
    Parses command-line arguments
    '''
    parser = argparse.ArgumentParser(description="Capture frames from a video.")
    parser.add_argument("file_path", help="Path to the video file.")
    parser.add_argument("-i", "--interval", type=int, default=1, help="Frame interval for capturing.")
    parser.add_argument("-d", "--directory", default="captured_frames", help="Directory to save captured frames.")
    return parser.parse_args()

if __name__ == '__main__':
    # Parse command-line arguments
    args = parse_arguments()

    # Check if the video file exists
    if not os.path.exists(args.file_path):
        print(f"Error: File '{args.file_path}' does not exist.")
        sys.exit(1)

    # Supported video formats check
    supported_formats = ('.mp4', '.avi', '.mov', '.mkv')
    if not args.file_path.lower().endswith(supported_formats):
        print("Warning: The file may not be a supported video format.")

    # Initialize FrameCapture and start capturing frames
    fc = FrameCapture(args.file_path, args.directory)
    fc.capture_frames(args.interval)

