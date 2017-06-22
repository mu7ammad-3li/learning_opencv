import cv2
import numpy as np 

img = cv2.imread('01.jpg',cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(150,150),(255,0,0),(15)) #BGR
cv2.rectangle(img,(15,25),(200,150),(0,0,255),5)
cv2.circle(img,(100,63),55,(0,255,0),-1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"hello world",(0,130),font,0.8,(0,255,255),5,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 