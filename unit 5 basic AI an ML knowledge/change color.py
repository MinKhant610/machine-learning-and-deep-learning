import cv2 as cv 
import matplotlib.pyplot as plt 

def main () :
    img = cv.imread ('images/min.jpg',1)

    img = cv.cvtColor (img,cv.COLOR_BGR2RGB)

    plt.imshow (img)
    plt.title ('Color')
    plt.xticks ([])
    plt.yticks ([])
    plt.show ()


main ()

