import cv2
#checking version
print(cv2.__version__)
mustangimg=cv2.imread('must.jpg',1)
print(mustangimg)
print(mustangimg.shape)
# 1 means colour in same channel --GRB OR RGB
# 0 No Colour Channel B&W --GRAY IMAGE in imread
# -1 maintaines image transparency
x,y,z=cv2.split(mustangimg)
'''cv2.imshow('drm',x)
cv2.waitKey(0)
cv2.imshow('drm',y)
cv2.waitKey(0)
cv2.imshow('drm',z)'''
#wait for window to close
cv2.line(mustangimg,(0,0),(800,800),(255,255,255),3)
cv2.rectangle(mustangimg,(100,100),(900,900),(255,0,255),6)
cv2.imshow('drm',mustangimg)
cv2.waitKey(0)