import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

def main ():

    img = cv.imread ('images/hero.jpg')
    img = cv.cvtColor (img,cv.COLOR_BGR2RGB)

    row , col , ch = img.shape

    R = cv.getRotationMatrix2D ((col/2,row/2),90,0.5)
    print (R)

    output = cv.warpAffine (img ,R, (col,row))

    plt.imshow (output)
    plt.title ('Rotation')
    plt.show () 

main () 