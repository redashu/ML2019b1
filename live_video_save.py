#!/usr/bin/python3

import  cv2
#  start camera
cap=cv2.VideoCapture(0)
#   video format / plugin  
video_plugin=cv2.VideoWriter_fourcc(*'XVID')
#  XVID  plugin  .mp4  .avi in some cases .mkv
#  now saving  video in a file
#   file name , plugin , FPS ,  resolution                                WIDTH , HEIGHT
output=cv2.VideoWriter('/home/fire/Desktop/adhoc3.avi',video_plugin,100,(640,480))

while cap.isOpened():
    status,frame=cap.read()
    cv2.imshow('live',frame)
    #  time for save 
    output.write(frame)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
output.release()  #  closing  file
cap.release()  #  closing  camera

