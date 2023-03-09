import cv2
import numpy as np
import imutils
import serial
import time
arduinoData = serial.Serial('COM3',9600,timeout = 1)
time.sleep(2)
bomb = 0
nub =38000
def nothing(x):
 pass
z = 0
def front():
 arduinoData.write(b'1')
def left():
 arduinoData.write(b'2')
def right():
 arduinoData.write(b'3')
def stop():
 arduinoData.write(b'4')
def rotate():
 arduinoData.write(b'5')
 time.sleep(0.5)
 
 
 
26
# url='http://192.168.19.55:8080/photo.jpg'
#cap=cv2.VideoCapture(0)
#font = cv2.FONT_HERSHEY_SIMPLEX
#bottomLeftCornerOfText = (10,500)
#fontScale = 1
#fontColor = (255,0,0)
#lineType = 2
c = 0
cap=cv2.VideoCapture("http://192.168.62.65:8080/video")
cv2.namedWindow("TB")
cv2.createTrackbar("L-H","TB",0,179,nothing)
cv2.createTrackbar("L-S","TB",0,255,nothing)
cv2.createTrackbar("L-V","TB",0,255,nothing)
cv2.createTrackbar("U-H","TB",179,179,nothing)
cv2.createTrackbar("U-S","TB",255,255,nothing)
cv2.createTrackbar("U-V","TB",255,255,nothing)
while True:
 #frame_resp = requests.get(url)
 #frame_arr = np.array(bytearray(frame_resp.content), dtype=np.uint8)
 #frame = cv2.imdecode(frame_arr,-1)
 _,frame=cap.read(
 hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 l_h = cv2.getTrackbarPos("L-H", "TB")
 l_s = cv2.getTrackbarPos("L-S", "TB")
 l_v = cv2.getTrackbarPos("L-V", "TB")
 u_h = cv2.getTrackbarPos("U-H", "TB")
 u_s = cv2.getTrackbarPos("U-S", "TB")
 u_v = cv2.getTrackbarPos("U-V", "TB")
 lower_red = np.array([43, 47, 47])
 upper_red = np.array([82, 246, 198])
27
 #lower_red = np.array([146, 76, 144])
 #upper_red = np.array([179, 255, 255]
 #lower_red = np.array([151, 149, 88])
 #upper_red = np.array([179, 255, 223])
 mask3 = cv2.inRange(hsv, lower_red, upper_red)
 #mask3 = cv2.erode(mask3,None,iterations=1)
 #mask3 = cv2.dilate(mask3,None,iterations=1)
 cnts3 = cv2.findContours(mask3, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
 cnts3 = imutils.grab_contours(cnts3)
 z = 0
 for c in cnts3:
 
 area3=cv2.contourArea(c)
 z = 0
 print (area3
 if area3>50:
 M = cv2.moments(c)
 cx = int(M["m10"]/M["m00"])
 cy = int(M["m01"]/M["m00"]
 if cx<400:
 left()
 print("Left")
 z = 1
 break
 elif cx>500:
 right()
 print("Right")
 z = 1
 break
 
 else:
28
 if area3<=nub:
 front()
 print("front")
 z = 1
 break
 
 else:
 bomb=bomb+1
 stop()
 print("stop")
 z = 0
 if bomb == 100:
 time.sleep(5)
 rotate()
 bomb = 0 
 nub = 27000
 break
 
 
 #cv2.circle(frame,(cx,cy),2,(255,255,255),-1)
 break
 if z == 0:
 stop()
 print("stop") 
 cv2.imshow('mask',mask3)
 cv2.imshow('frame',frame)
 key = cv2.waitKey(10)
 if key==27:
 break
cap.release()
cv2.destroyAllWindows()