import numpy as np
import cv2

img = cv2.resize(cv2.imread('nature.jpg',0),(0,0),fx=0.2,fy=0.3)
template = cv2.resize(cv2.imread('ball.jpg',0),(0,0),fx=0.5,fy=0.5)
img2 = img.copy()
h,w  = template.shape
print(img)

methods = [cv2.TM_CCOEFF,cv2.TM_CCOEFF_NORMED,cv2.TM_CCORR,cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]

for method in methods:
    img = img2.copy()
    result = cv2.matchTemplate(img2,template,method)
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)
    # print(min_loc)
    # print(max_loc)
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        location = max_loc
    else:
        location = max_loc

    bottom_right = (location[0]+w,location[1]+h)
    cv2.rectangle(img2,location,bottom_right,255,5)
    cv2.imshow("Match",img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()        
 