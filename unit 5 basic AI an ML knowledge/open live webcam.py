import cv2 as cv 

def main () :

    cap = cv.VideoCapture (0)

    print ('width' + str (cap.get(3)))
    print ('height' + str (cap.get(4)))

    cap.set (3 , 1024)
    cap.set (4 , 720)

    if cap.isOpened ():
        ret , frame = cap.read () 
    else :
        ret = False
    
    while (ret) :
        ret , frame = cap.read () 

        cv.imshow ('Live Video', frame)

        k = cv.waitKey (0)
        if k == 27 :
            break 
    
    cv.destroyAllWindows () 
    cap.release ()

main () 

