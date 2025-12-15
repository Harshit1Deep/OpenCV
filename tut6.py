import cv2
import random

img = cv2.imread('nature.jpg',1)
tag = img[500:700,600:900]
img[100:300,650:950] = tag
r = cv2.resize(img,(600,600))
cv2.imshow("Image",r)
cv2.waitKey(0)
cv2.destroyAllWindows()  