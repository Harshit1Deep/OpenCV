import cv2
img = cv2.imread("nature.jpg",1)
img = cv2.resize(img,(600,300))
# resized = cv2.resize(img,(0,0),fx=0.2,fy=0.2)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# import cv2
# img = cv2.imread("nature.jpg",1)
# img = cv2.resize(img,(600,300))
# # resized = cv2.resize(img,(0,0),fx=0.2,fy=0.2)
# rotated = cv2.rotate(img, cv2.ROTATE_180)
# cv2.imshow("Image",rotated)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
