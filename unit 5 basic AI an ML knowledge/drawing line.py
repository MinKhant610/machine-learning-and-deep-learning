import cv2 as cv
import numpy as np 

def main():
    img = np.zeros ((512,512,3) , np.uint8)
    cv.line(img,(0,0),(100,200),(0,255,0),2)
    cv.imshow ('Black',img)
    cv.waitKey (0)
    cv.destroyAllWindow()

if __name__ == '__main__':
    main()