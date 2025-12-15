import cv2
img = cv2.imread("paint3D.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray",gray)
# resize = cv2.resize(img,(350,300))
# cv2.imshow("paint",resize)
cv2.line(img, (0, 0), (300, 300), (0, 0, 255), 3)
cv2.waitKey(0)
# cv2.rectangle(img,(50,50),(700,700),(134,255,0),2)
