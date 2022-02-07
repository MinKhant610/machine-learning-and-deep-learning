import cv2 as cv 
import matplotlib.pyplot as plt 

def main () :
    
    img1 = cv.imread ('images/min.jpg')
    img2 = cv.imread ('images/linux_grey.jpg')

    img1 = cv.cvtColor (img1 , cv.COLOR_BGR2RGB)
    img2 = cv.cvtColor (img2 , cv.COLOR_BGR2RGB)
    
    add = img1 + img2 
    sub1 = img1 - img2 
    sub2 = img2 - img1 
    mul = img1 * img2 
    min50 = img1 + 50 
    tha_50 = img2 - 50 
    fifty = 50 - img1 
    division = img1 / img2 
    img3 = img1 * 1.5
    img4 = img2 / 1.5 

    images = [img1,img2,add,sub1,sub2,mul,min50,tha_50,fifty,division,img3,img4]
    title = ['MK','linux','MK+linux','MK-linux','linux-MK','MK*linux','+50','-50','50-MK','divide','*1.5','/1.5'] 

    for i in range (len(images)):
        plt.subplot (2,6,i+1)
        plt.imshow (images [i])
        plt.title (title[i])
        plt.xticks ([])
        plt.yticks ([])

    plt.show ()

    cv.waitKey (0)

main () 