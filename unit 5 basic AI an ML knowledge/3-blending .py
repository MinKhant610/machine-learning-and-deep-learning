import cv2 as cv 
import matplotlib.pyplot as plt 

def main () :

    img1 = cv.imread ('images/hero.jpg')
    img2 = cv.imread ('images/mask.jpg')

    img1 = cv.cvtColor (img1 ,cv.COLOR_BGR2RGB)
    img2 = cv.cvtColor (img2 ,cv.COLOR_BGR2RGB)

    alpha = 0.5
    beta = 0.5
    gamma =0.0

    output = img1 + img2 
    output2 = cv.addWeighted (img1,alpha,img2,beta,gamma)

    images = [img1,img2,output,output2]
    titles = ['img1','img2','img1 + img 2','blending']

    for i in range (4):
        plt.subplot (2,2,i+1)
        plt.imshow (images[i])
        plt.title (titles[i])
        plt.xticks([])
        plt.yticks ([])


    plt.show ()
    cv.waitKey (0)

main ()