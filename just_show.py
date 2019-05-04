#just display
import cv2
import numpy as np
import time
blue_L=(90,93,0)
blue_H=(148,255,199)
cam=cv2.VideoCapture(0)
img=cv2.imread('T1.jpg')
import pyttsx3
engine = pyttsx3.init()
print("Wassup shivam. Let's do something really cool.")
engine.say("Wassup shivam. Let's do something really cool.")
engine.runAndWait()
print("Okay so here we go.")
engine.say("Okay so here we go.")
engine.runAndWait()
print("Three...")
engine.say("Three...")
engine.runAndWait()
time.sleep(1)
print("Two...")
engine.say("Two...")
engine.runAndWait()
time.sleep(1)
print("One...")
engine.say("One...")
engine.runAndWait()
time.sleep(1)
print("Here we go!!!!!")
engine.say("Here we go!!!!!")
engine.runAndWait()
time.sleep(1)
while True:
    #img=image
    k=cv2.waitKey(1)
    _,frame=cam.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    ranged=cv2.inRange(hsv,blue_L,blue_H)
    final=cv2.add(img,frame)
    final2=cv2.bitwise_not(img,frame,mask=ranged)
    imgf=np.concatenate([final2,final],axis=1)
    cv2.imshow('HarryPotter Effect',imgf)
    if k & 0xFF==ord('q'):
        print("Time to say goodbye! Take care.")
        engine.say("Time to say goodbye! Take care.")
        engine.runAndWait()
        cam.release()
        cv2.destroyAllWindows()
        break
    
        
        


























