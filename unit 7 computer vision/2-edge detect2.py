import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

def main () :
    img = cv.imread ('images/coin1.jpeg')
    img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    blk = 101 
    con = 2 

    th = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,blk,con)

    medblur = cv.medianBlur(th,3)

    canny = cv.Canny(medblur,100,150,L2gradient=True)

    index , comp = cv.connectedComponents(canny)

    print ('Coins',index)

    while True :
        cv.imshow ('Canny',canny)

        k = cv.waitKey(10)
        if k == 27 :
            break 
    cv.destroyAllWindows() 

main () 