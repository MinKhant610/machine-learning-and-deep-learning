import cv2 as cv 
import matplotlib.pyplot as plt 

def main () :
    img = cv.imread ('images/min.jpg')

    plt.imshow (img)
    plt.show()

    plt.imshow (img , cmap = 'gray')
    plt.subplot (1,1)
    plt.title ('Gray Photo')
    plt.xticks ([])
    plt.yticks ([])
    plt.show ()

    
main ()