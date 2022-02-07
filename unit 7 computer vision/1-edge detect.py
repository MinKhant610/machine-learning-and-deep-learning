import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt 

img = cv.imread('images/coin2.jpeg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)


blk_size = 101
constant = 2 
th_img = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,blk_size,constant)

#smoothing 
medblur_img = cv.medianBlur(th_img,3)

#edge detect 
canny_img = cv.Canny (medblur_img,100,150,L2gradient=True)

cv.imshow ('Canny',canny_img)

(counts,_) = cv.findContours (canny_img.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

print ('Total Coins = {}'.format(len(counts)))

contour = img.copy() 

cv.drawContours (contour,counts,-1,(0,0,255),2)
cv.imshow('Coins',contour)

k = cv.waitKey(0)
if k == 27 :
    cv.destroyAllWindows()

