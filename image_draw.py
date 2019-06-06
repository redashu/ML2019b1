#!/usr/bin/python3

import  cv2
# checking version
print(cv2.__version__)
#  starting  camera
cap=cv2.VideoCapture('/home/fire/Desktop/wind.mp4') # here camera number fist

while cap.isOpened() :  #  return true or false  by checking camera status
    status,frame=cap.read()  #  starting  taking  frames or pictus
    #  time to draw a line 
    #    frame , start_point , end_point , color , width of line
    cv2.line(frame,(0,0),(200,250),(0,0,255),2)
    cv2.line(frame,(200,250),(400,250),(0,0,255),2)
    #  rectangle  
    cv2.rectangle(frame,(200,200),(300,300),(100,255,10),-1)
    #  circle 
    cv2.circle(frame,(150,150),50,(255,0,0),4)
    #  now display frame 
    cv2.imshow('live',frame)
    if  cv2.waitKey(10) & 0xff ==  ord('q'):
        #  here  ord is for converting  keys to ascii
        break
#  destroying all windows having frames
cv2.destroyAllWindows()
#  stoping camera 
cap.release()  #  now you can use the same camera with anther app 
