#static image filter
import cv2
def nothing(x):
    pass
#cv2.createWindow('HSV')
cv2.namedWindow('HSV')
cv2.createTrackbar('H','HSV',0,255,nothing)
cv2.createTrackbar('S','HSV',0,255,nothing)
cv2.createTrackbar('V','HSV',0,255,nothing)
cv2.createTrackbar('HM','HSV',0,255,nothing)
cv2.createTrackbar('SM','HSV',0,255,nothing)
cv2.createTrackbar('VM','HSV',0,255,nothing)
cv2.createTrackbar('R','HSV',0,255,nothing)
cv2.createTrackbar('G','HSV',0,255,nothing)
cv2.createTrackbar('B','HSV',0,255,nothing)
cv2.createTrackbar('RR','HSV',0,255,nothing)
cv2.createTrackbar('GG','HSV',0,255,nothing)
cv2.createTrackbar('BB','HSV',0,255,nothing)
signal=1
cam=cv2.VideoCapture(0)
while True:
    h=cv2.getTrackbarPos('H','HSV')
    s=cv2.getTrackbarPos('S','HSV')
    v=cv2.getTrackbarPos('V','HSV')
    hm=cv2.getTrackbarPos('HM','HSV')
    sm=cv2.getTrackbarPos('SM','HSV')
    vm=cv2.getTrackbarPos('VM','HSV')
    r=cv2.getTrackbarPos('R','HSV')
    g=cv2.getTrackbarPos('G','HSV')
    b=cv2.getTrackbarPos('B','HSV')
    rr=cv2.getTrackbarPos('RR','HSV')
    gg=cv2.getTrackbarPos('GG','HSV')
    bb=cv2.getTrackbarPos('BB','HSV')
    if signal==1:
        _,frame=cam.read()
    k=cv2.waitKey(1)
    if k==ord('c'):
        signal=2
    if signal==2:
        lower1=(h,s,v)
        upper1=(hm,sm,vm)
        lower=(r,g,b)
        upper=(rr,gg,bb)
        image_bgr=cv2.inRange(frame,lower,upper)
        cv2.imshow('image_bgr',image_bgr)
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        hsvx=cv2.inRange(hsv,lower1,upper1)
        cv2.imshow('hsv',hsvx)
    cv2.imshow('frame',frame)
        
        
