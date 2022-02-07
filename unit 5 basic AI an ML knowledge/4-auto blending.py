import cv2 as cv 
import matplotlib.pyplot as plt 
import numpy as np
import time

def main () :
    img1 = cv.imread ('images/hero.jpg')
    img2 = cv.imread ('images/mask.jpg')

    img1 = cv.cvtColor (img1,cv.COLOR_BGR2RGB)
    img2 = cv.cvtColor (img2,cv.COLOR_BGR2RGB)

    alpha = 0
    beta = 1.0
    gamma = 0

    for i in np.linspace (0,1,100):
        alpha = i 
        beta = 1 - i
        
        output = cv.addWeighted (img1,alpha,img2,beta,gamma)
        cv.imshow ('Transition',output)
        time.sleep (0.05)

        if cv.waitKey (1) == 27 :
            break 
    cv.destroyAllWindows () 
main () 