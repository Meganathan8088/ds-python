import cv2

video_path = r"C:\Users\flipkart\Downloads\Cars Moving On Road Stock Footage - Free Download.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("End of video.")
        break

    cv2.imshow("Video", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
