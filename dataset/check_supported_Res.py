

import cv2

# Open the webcam
cap = cv2.VideoCapture(1)  # Use 0 for the default camera

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Get the maximum resolution supported by the camera
max_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
max_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f"Maximum Resolution: {max_width}x{max_height}")

# Release the camera
cap.release()