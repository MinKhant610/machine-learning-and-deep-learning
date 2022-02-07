import cv2 as cv 
import numpy as np 

def Bfunc ():
    pass

def Gfunc ():
    pass

def Rfunc ():
    pass

def main ():
    img = np.zeros ((512,512,3),np.uint8)
    window = 'OpenCv'
    cv.namedWindow (window)
    
    cv.createTrackbar('B',window,0,255,Bfunc)
    cv.createTrackbar('G',window,0,255,Gfunc)
    cv.createTrackbar('R',window,0,255,Rfunc)

    while True:
        cv.imshow (window,img)
        blue = cv.getTrackbarPos ('B',window)
        green = cv.getTrackbarPos ('G',window)
        red = cv.getTrackbarPos ('R',window)

        img [:] = [blue,green,red]
        print (blue,green,red)

        if cv.waitKey(1) == 27:
            break 

    cv.destroyAllwindows()

if __name__ == '__main__':
    main()
