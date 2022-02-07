import cv2 as cv 
 
def main () :
    name = 'Video Player'
    cv.namedWindow (name)

    cap = cv.VideoCapture ('test.mp4')

    while cap.isOpened():
        ret , frame = cap.read ()

        if (ret) :
            cv.imshow (name , frame)
            
            k = cv.waitKey (44)
            if k == 27 :
                break 
        else :
            break 
    
    cv.destroyAllwindows ()
    cap.release()

main ()
