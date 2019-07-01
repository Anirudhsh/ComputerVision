import cv2
import numpy as np


def img_diff(x,y,z):
    
    #diff b/w x,y = d1
    d1 = cv2.absdiff(x,y)
    #diff b/w y,z = d2
    d2 = cv2.absdiff(x,y)
    #diff b/w x,z = d3
    #d3 = cv2.absdiff(x,y)
    finalimg = cv2.bitwise_and(d1,d2)
    return finalimg


cap = cv2.VideoCapture(0)
#status,frame = cap.read()
tp1 = cap.read()[1]
tp2 = cap.read()[1]
tp3 = cap.read()[1]
# To make more accurate conv all to grayscale
gray1 = cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY)
'''
print(gray1)
print(gray2)
print(gray3)
'''
while cap.isOpened():
    status,frame=cap.read()
    motionimg = img_diff(gray1,gray2,gray3)
    # replacing image frame
    gray1 = gray2
    gray2 = gray3
    gray3 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Live',frame)
    cv2.imshow('Motion',motionimg)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()


    