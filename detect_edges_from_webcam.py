# import the necessary packages
import numpy as np
import cv2
cap_stream = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'H264')
out = cv2.VideoWriter('Output1.mkv', fourcc ,20.0 ,(640,480),False)

 
def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
 
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
 
	# return the edged image
	return edged
while(cap_stream.isOpened()):
    ret, image = cap_stream.read()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    wide = cv2.Canny(blurred, 10, 200)
    tight = cv2.Canny(blurred, 225, 250)
    auto = auto_canny(blurred)
    cv2.imshow('wide',wide)
    cv2.imshow('tight',tight)
    cv2.imshow('auto',auto)
    out.write(auto)
    if cv2.waitKey(1) & 0xFF== ord('q'): 
        break
out.release() 
cap_stream.release()
cv2.destroyAllWindows()
