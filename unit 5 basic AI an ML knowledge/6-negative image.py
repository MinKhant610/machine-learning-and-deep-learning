import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

def main () :

    img = cv.imread ('images/security.jpeg')

    img1 = cv.cvtColor (img,cv.COLOR_BGR2RGB)
    img2 = cv.cvtColor (img,cv.COLOR_BGR2GRAY)

    img3 = 255 - img1
    img4 = 255 - img2 

    images = [img1, img2, img3 , img4]
    title = ['security','gray','255-security','255-gray']

    for i in range (4):
        plt.subplot (2,2,i+1)
        plt.imshow (images[i],cmap='gray')
        plt.title (title[i])
        plt.xticks ([])
        plt.yticks ([])

    plt.show () 

main ()