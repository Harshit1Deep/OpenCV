import cv2
img = cv2.imread("nature.jpg",1)
# print(img)
print(type(img))
print(img.shape)
print(img[0])
print(img[257])
cv2.waitKey(0)
cv2.destroyAllWindows()
