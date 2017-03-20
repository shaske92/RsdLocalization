# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 17:10:39 2017

@author: sara
"""

import cv2 
import numpy as np

im = cv2.imread('greyscale.png',0)

#intensitet = im.at<uchar>(156, 228)


ret, thr = cv2.threshold(im, 150, 255, 0)
cv2.imwrite('BW.png', thr)


img = cv2.imread('BW.png')
kernel = np.ones((4,4),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
closing = cv2.morphologyEx(erosion, cv2.MORPH_CLOSE, kernel)

cv2.imwrite('map.png', closing)
cv2.imshow("map", closing)            
cv2.waitKey()
            
    


