import cv2
#checking version
print(cv2.__version__)
mustangimg=cv2.imread('must.jpg',1)
print(mustangimg)
print(mustangimg.shape)
# 1 means colour in same channel --GRB OR RGB
# 0 No Colour Channel B&W --GRAY IMAGE in imread
# -1 maintaines image transparency
cv2.imshow('drm',mustangimg[400:830,400:850])
#wait for window to close
cv2.waitKey(0)