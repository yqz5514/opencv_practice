import numpy as np
import cv2

black = np.zeros([150,200,1],'uint8') # 150 pixels tall, 200 pixels width, 1 channel, and utin8(u:unsigned, int8: power of 8, this indicates the range of value allowed in this matrix will be 0 to 255) indicate type of image.
cv2.imshow("Black",black)# show this image, window assigned black
print(black[0,0,:])

ones = np.ones([150,200,3],'uint8')
cv2.imshow("Ones",ones)
print(ones[0,0,:])


white = np.ones([150,200,3],'uint16')
white *= (2**16-1)
cv2.imshow("White",white)
print(white[0,0,:])

color = ones.copy()
color[:,:] = (255,0,0)
cv2.imshow("Blue",color)
print(color[0,0,:])

cv2.waitKey(0)
cv2.destroyAllWindows()