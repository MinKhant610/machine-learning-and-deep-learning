import cv2 as cv 
import matplotlib.pyplot as plt 

def main () :

    img1 = cv.imread ('images/hero.jpg')
    img2 = cv.imread ('images/mask.jpg')

    img1 = cv.cvtColor (img1 , cv.COLOR_BGR2RGB)
    img2 = cv.cvtColor (img2 , cv.COLOR_BGR2RGB)

    img3 = cv.bitwise_not (img1)
    img4 = cv.bitwise_and (img1,img2)
    img5 = cv.bitwise_or (img1,img2)
    img6 = cv.bitwise_xor (img1,img2)

    images = [img1 , img2 , img3 , img4 , img5 , img6]
    titles = ['hero','mask','not','and','or','xor']

    for i in range (6):
        plt.subplot (2,3,i+1)
        plt.imshow (images[i])
        plt.title (titles[i])
        plt.xticks ([])
        plt.yticks ([])

    plt.show ()

main ()