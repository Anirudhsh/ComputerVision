import cv2
import pandas as pd
import numpy as np
print(cv2.__version__)
sub = cv2.imread("subaru.jpg")# image1
lam = cv2.imread("lambo.jpg")# image 2
temp1 = cv2.imread("subaru.jpg")# image1
temp2 = cv2.imread("lambo.jpg")# image 2
#cv2.imshow("LAMBORGINI",lam)
#cv2.imshow("SUBARU",sub)
if sub.shape != lam.shape: #resolution of both the images should be same
    print("size of images not equal")
else:
    rc = sub.shape
    #print(rc[2])
    #print(sub)
    #print(type(sub))
    r = np.random.randint(0,rc[0]-9)
    c = np.random.randint(0,rc[1]-19)
    print(rc)
    cv2.imshow("BEFORE_LAM",lam)
    cv2.imshow("BEFORE_SUB",sub)
    #temp1=np.zeros((rc[0],rc[1],3),np.uint8)
    #temp2=np.zeros((rc[0],rc[1],3),np.uint8)
    #print(temp1.shape)
    temp1[r:r+10,c:c+20]=lam[r:r+10,c:c+20]
    temp2[r:r+10,c:c+20]=sub[r:r+10,c:c+20]
    
    #print("___________________")
    #print(temp2)
    cv2.imshow("AFTER_LAM",temp1)
    cv2.imshow("AFTER_SUB",temp2)
    cv2.waitKey(0)
