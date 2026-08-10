import cv2

# Store the points of the line
points = []

# Mouse callback function
def draw_line(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))

# Open webcam
cap = cv2.VideoCapture(0)

cv2.namedWindow("Webcam")
cv2.setMouseCallback("Webcam", draw_line)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Unable to access webcam")
        break

    # Draw lines between points
    for i in range(1, len(points)):
        cv2.line(frame, points[i - 1], points[i], (0, 255, 0), 3)

    cv2.imshow("Webcam", frame)

    # Press 'c' to clear all lines
    # Press 'q' to quit
    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        points.clear()

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
