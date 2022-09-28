>>> import numpy as np
>>> import cv2
>>> img = cv2.imread("opencv-logo.png", 1)# 1 means want the origina color of picture, 0 indicates blacka  nd white
>>> 
>>> img
array([[[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ..., 
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ..., 
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ..., 
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       ..., 
       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ..., 
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ..., 
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ..., 
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]]], dtype=uint8)
# pixels
>>> type(img)
<class 'numpy.ndarray'>
>>> len(img)
739 # number of horizontal rows
>>> len(img[0])
600 # verical columns
>>> len(img[0][0])
3 # channels found in pictures in this one is R,G, and B channel
>>> img.shape
(739, 600, 3)
>>> img.dtype
dtype('uint8') # unassigned interger value of 8
>>> 2**8 # a maxium of two to the eright values in each pixel
256 # and the range of values vary from 0 to 255
>>> img[10, 5] # 10th row, 5th column
array([255, 255, 255], dtype=uint8) # pixel value at the array, given that our image has a 
# maximm value of 255 of image, this is perfectly white
>>> img[:, :, 0] # onw channel image
array([[255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       ..., 
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255]], dtype=uint8)
>>> img.size # total number of pixels in image
1330200