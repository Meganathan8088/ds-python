import cv2
import numpy as np

# Create a black image
image = np.zeros((500, 500, 3), dtype=np.uint8)

drawing = False
start_x, start_y = -1, -1

# Mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global drawing, start_x, start_y, image

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_x, start_y = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            temp = image.copy()
            cv2.rectangle(temp, (start_x, start_y), (x, y), (0, 255, 0), 2)
            cv2.imshow("Draw Rectangle", temp)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(image, (start_x, start_y), (x, y), (0, 255, 0), 2)
        cv2.imshow("Draw Rectangle", image)

# Create window
cv2.namedWindow("Draw Rectangle")
cv2.setMouseCallback("Draw Rectangle", draw_rectangle)

# Display window
while True:
    cv2.imshow("Draw Rectangle", image)

    key = cv2.waitKey(1) & 0xFF

    # Press 'c' to clear the screen
    if key == ord('c'):
        image = np.zeros((500, 500, 3), dtype=np.uint8)

    # Press 'q' to quit
    elif key == ord('q'):
        break

cv2.destroyAllWindows()
