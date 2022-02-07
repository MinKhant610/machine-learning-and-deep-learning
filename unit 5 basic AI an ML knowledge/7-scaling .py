import cv2 as cv 

def main () :
    
    img = cv.imread ('images/security.jpeg')

    linear = cv.resize (img,None , fx=1.5 , fy=1.5 , interpolation= cv.INTER_LINEAR)
    cubic = cv.resize (img,None , fx=2 , fy=2 , interpolation= cv.INTER_CUBIC)
    area = cv.resize (img,None , fx=1.2 , fy=1.2 , interpolation= cv.INTER_AREA)
    nearest = cv.resize (img,None , fx=3 , fy=1.0 , interpolation= cv.INTER_NEAREST)

    cv.imshow ('Security',img)
    cv.imshow ('linear',linear)
    cv.imshow ('cubic',cubic)
    cv.imshow ('area',area)
    cv.imshow ('nearest',nearest)

    if cv.waitKey(0) == 27 :
        cv.destroyAllWindows () 


main () 