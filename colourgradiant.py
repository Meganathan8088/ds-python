import cv2
import numpy as np

image = np.zeros((500, 600, 3), dtype=np.uint8)

for x in range(600):
    if x < 200:  # Red to Green
        r = 255 - int(x * 255 / 200)
        g = int(x * 255 / 200)
        b = 0
    elif x < 400:  # Green to Blue
        r = 0
        g = 255 - int((x - 200) * 255 / 200)
        b = int((x - 200) * 255 / 200)
    else:  # Blue to Red
        r = int((x - 400) * 255 / 200)
        g = 0
        b = 255 - int((x - 400) * 255 / 200)

    image[:, x] = (b, g, r)  # OpenCV uses BGR

cv2.imshow("RGB Rainbow Gradient", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
