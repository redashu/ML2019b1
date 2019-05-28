#!/usr/bin/python3

import  cv2
import  matplotlib.pyplot as plt
# import computer vision build in  c++ lang
#  reading  image  data
read_ops=[i for  i in dir(cv2) if 'read' in i]
print(read_ops)

#  reading  data from image
img=cv2.imread('cat.jpg',1)  #  loading  original image
crop=img[0:200,50:300]


plt.imshow(img)
cv2.imshow('trans',img)
cv2.imshow('crop',crop)
# to hold  image window
cv2.waitKey(0)
#  destroying  windows
cv2.destroyAllWindows()
