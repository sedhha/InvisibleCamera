#HARRY POTTER
import pyttsx3
engine = pyttsx3.init()
engine.say("Wassup shivam. Let's do this.")
engine.runAndWait()
#print('Done')
import cv2
blueL=(0,0,0)
cam=cv2.VideoCapture(0)
print('Calibrate background now.')
import time
time.sleep(5)
ret,calib=cam.read()
cv2.imshow('Calib',calib)
engine.say('Calibrated Image is ready')
engine.runAndWait()
cv2.imwrite('T1.jpg',calib)
