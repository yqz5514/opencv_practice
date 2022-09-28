import numpy as np
import cv2
 
img = cv2.imread("opencv-logo.png")
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
cv2.imshow("Image",img)
cv2.waitKey(0) # waitkay function will capture the key pressed on the keyboard 
cv2.imwrite("output.jpg",img)
