import cv2 as cv 
import matplotlib.pyplot as plt 

def main () :

    cap = cv.VideoCapture (0)

    ret , frame = cap.read () 

    if cap.isOpened () :
        ret , frame = cap.read () 
        
        print (ret)

    img = cv.cvtColor ( frame , cv.COLOR_BGR2RGB)

    plt.imshow (img)
    plt.show () 

    cap.release () 

main () 