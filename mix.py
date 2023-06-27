import cv2
import numpy as np

# Constants for defining colors
COLOR_BLUE = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_RED = (0, 0, 255)
COLOR_YELLOW = (0, 255, 255)

# Initialize canvas
canvas = np.ones((480, 640, 3), dtype=np.uint8) * 255

# Initialize rectangle parameters
rect_start = None
rect_end = None
is_drawing = False

def draw(event, x, y, flags, param):
    global rect_start, rect_end, is_drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        rect_start = (x, y)
        is_drawing = True
    
    if event == cv2.EVENT_LBUTTONUP:
        rect_end = (x, y)
        cv2.rectangle(canvas, rect_start,  rect_end, COLOR_BLUE, 2)
        cv2.imshow('Paint', canvas)
        is_drawing = False
        

    if event == cv2.EVENT_MOUSEMOVE:
        if is_drawing:
            canvas_copy = canvas.copy()
            cv2.rectangle(canvas_copy, rect_start, (x, y), COLOR_BLUE, 2)
            cv2.imshow('Paint', canvas_copy)
            cv2.waitKey(100)

# Create a named window and bind the mouse event handler
cv2.namedWindow('Paint')
cv2.setMouseCallback('Paint', draw)

while True:
    # Display the canvas
    cv2.imshow('Paint', canvas)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release all windows
cv2.destroyAllWindows()