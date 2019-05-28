#!/usr/bin/python3

import  cv2

# describing  version
print(cv2.__version__)

#  search for  camera handling  function 
x=[i for  i  in  dir(cv2) if  'Video' in i]
print(x)

#  starting  videocapture 
cap=cv2.VideoCapture('/home/fire/Desktop/wind.mp4')  #  data live , stored , streamed 
print(dir(cap))  #  exploring  camera ops

# checking camera  start point
while  cap.isOpened()  :
    status,img=cap.read()
    #  changing image  gray scale   
    cv2.imshow('gray',img)
    #    10 ms window close  keyborad action capture ,  ord ==ascii values --q
    if cv2.waitKey(10)  &  0xff == ord('q') :  #  this  is True
        break
cv2.destroyAllWindows()
cap.release()




