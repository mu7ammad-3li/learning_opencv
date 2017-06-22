import cv2 
import numpy as np 
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'H264')
out=cv2.VideoWriter('out.mkv',fourcc,20.0,(640,480),False ) 
while True: 
    _ ,frame = cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(gray)
    cv2.imshow('gray',gray)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q') : 
        break 
out.realease()
cap.realease()
cv2.destroyAllWindows()
