import cv2 as cv 
import matplotlib.pyplot as plt 
import numpy as np 

def main () :

    img = cv.imread ('images/hero.jpg')
    img = cv.cvtColor (img ,cv.COLOR_BGR2RGB)

    row , col , ch = img.shape 

    point1 = np.float32 ([[0,0],[300,0],[0,300],[300,300]])
    point2 = np.float32 ([[0,0],[100,0],[0,100],[100,100]])

    P = cv.getPerspectiveTransform(point1 , point2)
    print (P)

    output = cv.warpPerspective (img , P , (500,500) )

    plt.imshow (output)
    plt.title ('Perspective Transform')
    plt.show () 

main () 