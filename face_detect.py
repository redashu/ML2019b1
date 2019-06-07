#!/usr/bin/python3

import cv2
# loading  face trained  data
facehaar=cv2.CascadeClassifier('face.xml')

# image read  #  plz operate all operation in  gray scale
virat_img=cv2.imread('virat.jpg')
print(virat_img.shape)

#  face detector  apply in  virat_img--scalling  range 
face_only=facehaar.detectMultiScale(virat_img,1.15,5)
print(face_only)
for  x,y,w,h in  face_only:
	cv2.rectangle(virat_img,(x,y),(x+w,y+h),(0,0,255),2)



#  its normal display 
cv2.imshow('all',virat_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
