import cv2
import numpy as np 
image=cv2.imread('01.jpg',cv2.IMREAD_COLOR)
roi=image[100:500,100:500]
#image[100:500,100:500] [255,255,255]
#print(roi)
cv2.imshow('image',image)
cv2.imshow('roi',roi)
cv2.waitKey(0)
cv2.destroyAllWindows() 