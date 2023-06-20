import cv2
import numpy as np

# Constants for defining colors
COLOR_BLUE = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_RED = (0, 0, 255)
COLOR_YELLOW = (0, 255, 255)

# Initialize canvas
canvas = np.ones((480, 640, 3), dtype=np.uint8) * 255

# Initialize marker position
marker_position = None

def draw(event, x, y, flags, param):
    global marker_position

    if event == cv2.EVENT_LBUTTONDOWN:
        marker_position = (x, y)
    
    if event == cv2.EVENT_LBUTTONUP:
        marker_position = None

    if event == cv2.EVENT_MOUSEMOVE:
        if marker_position is not None:
            cv2.circle(canvas, (x, y), 5, COLOR_BLUE, -1)

# Create a named window and bind the mouse event handler
cv2.namedWindow('Paint')
cv2.setMouseCallback('Paint', draw)

# Start video capture from the default camera
capture = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = capture.read()

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper boundaries for the marker color
    lower_color = np.array([20, 100, 100])
    upper_color = np.array([40, 255, 255])

    # Threshold the HSV image to get only the marker color
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        # Find the largest contour
        max_contour = max(contours, key=cv2.contourArea)

        # Find the centroid of the largest contour
        M = cv2.moments(max_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            marker_position = (cx, cy)

    if marker_position is not None:
        # Draw a circle at the marker position
        cv2.circle(frame, marker_position, 5, COLOR_GREEN, -1)

    # Display the frame and the canvas
    cv2.imshow('Paint', np.hstack((frame, canvas)))

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
capture.release()
cv2.destroyAllWindows()