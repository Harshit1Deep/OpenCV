import cv2
import random

img = cv2.imread('nature.jpg',1)
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = random.randint(0,255),random.randint(0,255),random.randint(0,255)

r = cv2.resize(img,(600,400))
cv2.imshow("Image",r)
cv2.waitKey(0)
cv2.destroyAllWindows()        