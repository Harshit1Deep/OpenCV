import numpy as np
import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Camera not opened")
    exit()
while True:
    ret,frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    image = np.zeros(frame.shape,np.uint8)
    smaller_frame = cv2.resize(frame,(400,600))
    image[:height//2,:width//2] = cv2.rotate(smaller_frame,cv2.ROTATE_180) 
    image[height//2,:width//2] = smaller_frame
    image[:height//2,width//2:] = cv2.rotate(smaller_frame,cv2.ROTATE_180) 
    image[height//2:,width//2:] = smaller_frame
    if not ret:
        print("Failed to grab frame")
        break
    cv2.imshow("Frame",image)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()  

# 90 clockwise and counterclockwise can't rotate