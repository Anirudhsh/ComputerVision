import cv2
import sys
#checking version
print(cv2.__version__)
data = sys.argv[1]
img=cv2.imread(data,1)
cv2.imshow("w1",img)
cv2.waitKey(0)
img1=cv2.imread(data,0)
#saving image
cv2.imwrite('newdog.jpg',img1)
print(img)