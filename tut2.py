import cv2
img = cv2.imread("nature.jpg",1)
img = cv2.resize(img,(600,300))
cv2.imwrite("Nature.png",img)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
