#!/usr/bin/python3

import  cv2
# checking version
print(cv2.__version__)
#  starting  camera
cap=cv2.VideoCapture(0) # here camera number fist

while cap.isOpened() :  #  return true or false  by checking camera status
    status,frame=cap.read()  #  starting  taking  frames or pictus
    #  now converting  to gray scale
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # chechking  frame size
    print(frame.shape)
    #  now display frame 
    cv2.imshow('live',frame)
    cv2.imshow('live1',gray_frame)
    cv2.imshow('live2',hsv_frame)
    if  cv2.waitKey(10) & 0xff ==  ord('q'):
        #  here  ord is for converting  keys to ascii
        break
#  destroying all windows having frames
cv2.destroyAllWindows()
#  stoping camera 
cap.release()  #  now you can use the same camera with anther app 
