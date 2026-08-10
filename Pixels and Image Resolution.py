import cv2

# Read image
image = cv2.imread(r"C:\Users\flipkart\OneDrive\Desktop\Elsa.jpg")

# Image resolution
height, width = image.shape[:2]

print("Image Width :", width, "pixels")
print("Image Height:", height, "pixels")
print("Resolution  :", width * height, "pixels")

# Pixel value at (100,100)
pixel = image[100, 100]

print("Pixel value at (100,100):", pixel)
print("Blue :", pixel[0])
print("Green:", pixel[1])
print("Red  :", pixel[2])

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
