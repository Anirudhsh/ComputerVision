import cv2
import sys
import time
#checking version
print(cv2.__version__)
#checking video modules
print([i for i in dir(cv2) if 'Video' in i ])
cap = cv2.VideoCapture(0)

#  first Camera
# To check camera started or not
if cap.isOpened() :
    print("Camera Ready")
else:
    print("Check Your Webcam drivers")
status,img=cap.read()
time.sleep(1)
status1,img1=cap.read()
cv2.imshow('liveimg',img)
cv2.imshow('liveimg1',img1)
cv2.waitKey(0)

#to close camera
cap.release()
