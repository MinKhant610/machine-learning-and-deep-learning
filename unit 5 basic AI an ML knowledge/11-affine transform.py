import cv2 as cv 
import matplotlib.pyplot as plt 
import numpy as np 

def main () :

    img = cv.imread ('images/hero.jpg')
    img = cv.cvtColor (img ,cv.COLOR_BGR2RGB)

    row , col , ch = img.shape 

    point1 = np.float32 ([[100,100],[300,100],[100,300]])
    point2 = np.float32 ([[250,150],[400,150],[400,300]])

    A = cv.getAffineTransform (point1 , point2)
    print (A)

    output = cv.warpAffine (img , A , (col,row))

    plt.imshow (output)
    plt.title ('Affine Transform')
    plt.show () 

main () 
    
