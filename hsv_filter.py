#HSV contouring
import numpy as np
import cv2
def nothing(x):
    pass
cv2.namedWindow('Properties')
cv2.resizeWindow('Properties',400,400)
cv2.createTrackbar('H','Properties',0,255,nothing)
cv2.createTrackbar('S','Properties',0,255,nothing)
cv2.createTrackbar('V','Properties',0,255,nothing)
cv2.createTrackbar('HM','Properties',0,255,nothing)
cv2.createTrackbar('SM','Properties',0,255,nothing)
cv2.createTrackbar('VM','Properties',0,255,nothing)
cam=cv2.VideoCapture(0)
a_L=np.array([67,174,99])
a_U=np.array([133,227,169])
while True:
    _,frame=cam.read()
    frame2= cv2.GaussianBlur(frame,(5,5),0)
    k=cv2.waitKey(1)
    h=cv2.getTrackbarPos('H','Properties')
    s=cv2.getTrackbarPos('S','Properties')
    v=cv2.getTrackbarPos('V','Properties')
    hm=cv2.getTrackbarPos('HM','Properties')
    sm=cv2.getTrackbarPos('SM','Properties')
    vm=cv2.getTrackbarPos('VM','Properties')

    #print(h,s,v,hm,sm,vm)
    a_L=np.array([h,s,v])
    a_U=np.array([hm,sm,vm])
    #print(type(frame))
    #print(a_L)
    #print(a_U)
    grab=cv2.inRange(frame2,a_L,a_U)
    (_,contours,_) = cv2.findContours(grab,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
    try:
        c = max(contours,key=cv2.contourArea)
        imgf=cv2.drawContours(frame, [c], 0, (0,255,0), 3)
        cv2.imshow('frame2',imgf)
    except:
        pass
    cv2.imshow('frame',grab)
    cv2.imshow('frame1',frame)

