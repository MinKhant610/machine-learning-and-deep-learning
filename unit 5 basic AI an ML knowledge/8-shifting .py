import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

def main ():

    img = cv.imread ('images/mask.jpg')
    img = cv.cvtColor (img,cv.COLOR_BGR2RGB)

    row , col , channels = img.shape 

    T = np.float32 ([[1,0,100],[0,1,50]])
    print (T)

    output = cv.warpAffine (img,T,(col,row))

    plt.imshow (output)
    plt.title ('Shifting')
    plt.show () 

main ()