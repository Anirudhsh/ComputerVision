import cv2
import sys
import time
#checking version
print(cv2.__version__)
#checking video modules
print([i for i in dir(cv2) if 'Video' in i ])
cap = cv2.VideoCapture(0)

#adding plugin for contonous frame saving
plugin = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('class.avi',plugin,20,(640,480))

while cap.isOpened() :
    status,frame = cap.read()
    #cv2.imshow('live',frame)
    frame1=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #cv2.line(frame,(0,0),(200,300),(0,255,0),3)
   # cv2.rectangle(frame,(50,100),(300,400),(0,0,255),3)
    cv2.circle(frame,(500,200),120,(13,44,123),2)
    font=cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(frame,"TONY MKL",(10,400),font,4,(0,0,255),4,cv2.LINE_AA)
    cv2.imshow('livegray',frame)
    output.write(frame) #sending data to VideoWrite
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
#to close camera
cap.release()
