#!/usr/bin/python3

import cv2
cap=cv2.VideoCapture(0)

tp1=cap.read()[1]
tp2=cap.read()[1]
tp3=cap.read()[1]
#  grayscale
gray1=cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)
gray3=cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY)

#  create  image diff function
def  image_diff(x,y,z):
	imgdiff1=cv2.absdiff(x,y)
	imgdiff2=cv2.absdiff(y,z)
	finalimgdiff=cv2.bitwise_and(imgdiff1,imgdiff2)
	return  finalimgdiff


#  continue camera
while cap.isOpened(): 
	status,frame=cap.read()
	#  calling  function 
	image_abs=image_diff(gray1,gray2,gray3)
	gray1=gray2
	gray2=gray3
	gray3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('motion',frame)
	cv2.imshow('motion1',image_abs)
	print(image_abs)
	if cv2.waitKey(10)  & 0xff == ord('q') :
		break

cv2.waitKey(0)
cv2.destroyAllWindows()
