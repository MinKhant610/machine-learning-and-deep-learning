import cv2 as cv 
import matplotlib.pyplot as plt 

def main () :

    img1 = cv.imread ('images/min.jpg')
    img2 = cv.imread ('images/aa.jpeg')

    img1 = cv.cvtColor (img1 , cv.COLOR_BGR2RGB)
    img2 = cv.cvtColor (img2 , cv.COLOR_BGR2RGB)

    plt.subplot (1,2,1)
    plt.imshow (img1)
    plt.title ('Min Khant')
    plt.xticks ([])
    plt.yticks ([])

    plt.subplot (1,2,2)
    plt.imshow (img2)
    plt.title ('Jarvis')
    plt.xticks ([])
    plt.yticks ([])

    plt.show ()

main ()
