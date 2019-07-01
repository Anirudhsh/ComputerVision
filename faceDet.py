import cv2

cap = cv2.VideoCapture(0)
# Loading Face Data
casclf = cv2.CascadeClassifier('face.xml')
while cap.isOpened():
    status,frame = cap.read()
    # now we can apply calssifier in live frame
    face = casclf.detectMultiScale(frame,1.5,5)   # classifier tuning par
    #print(face)
    for x,y,h,w in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow('Live',frame)
        # only face now
        #facedata = frame[x:x+h,y:y+h]
        #cv2.imshow('FaceOnly',facedata)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()