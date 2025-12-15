import cv2
import numpy as np

# img = np.zeros((199, 200, 3), dtype=np.uint8)
# cv2.imshow("Test", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# img = cv2.imread("paint3D.png")

# cv2.imshow("My Picture", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# Load the Haar cascade file
cascade_path = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

# Load your image
img = cv2.imread("paint3D.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show the result
cv2.imshow("Detected Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

