import cv2

image = cv2.imread(r"C:\Users\flipkart\OneDrive\Desktop\Elsa.jpg")

# Resize image
resized = cv2.resize(image, (800, 500))

cv2.imshow("Image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
