
import cv2
import numpy as np 
#--------------------------------------------
image1=cv2.imread('rosesd1.jpg')
image2=cv2.imread('rosesd2.jpg')

#add =image1 + image2
#weighted = cv2.addWeighted(image1,0.6,image2,0.4,0)
rows,cols,channels=image2.shape
roi = image1[0:rows,0:cols]
image2gray = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(image2gray,50,255, cv2.THRESH_BINARY_INV) 
cv2.imshow('MASK',mask)



#--------------------------------------------
cv2.waitKey(0)
cv2.destroyAllWindows() 