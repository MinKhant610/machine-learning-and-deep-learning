import numpy as np 
import matplotlib.pyplot as plt 
import time 
import cv2 as cv 

def main () :

    img = cv.imread ('images/mask.jpg')

    name = 'image rortation'
    cv.namedWindow (name)

    row , col , ch = img.shape 

    angle = 0 

    while True :
        if angle == 360 :
            angle = 0 
        
        R = cv.getRotationMatrix2D ((col/2,row/2),angle,1)
        print (R)

        output = cv.warpAffine (img , R , (col , row ))

        cv.imshow (name , output )
        angle = angle + 1 
        time.sleep (0.01)

        if cv.waitKey (1) == 27 :
            break 
    
    cv.destroyAllWindows () 

main () 
