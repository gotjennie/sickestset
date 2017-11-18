import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('setboard.jpg')
img_rgb = cv2.resize(img_rgb,(0,0), fx=0.1, fy=0.1)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)


for i in range(1):    
    template = cv2.imread('cards/3OPH.png',0)
    template = cv2.resize(template,(0,0), fx=0.1, fy=0.1)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print max_loc
    #cv2.circle(img_rgb, max_loc, 20,(0,0,255))
    cv2.rectangle(img_rgb, max_loc, (max_loc[0]+w, max_loc[1]+h), (0,0,255), 2)

#    threshold = 0.8
#    loc = np.where( res >= threshold)
#    for pt in zip(*loc[::-1]):
#        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    
#cv2.imshow('res', img_rgb)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imwrite('res.png',img_rgb)