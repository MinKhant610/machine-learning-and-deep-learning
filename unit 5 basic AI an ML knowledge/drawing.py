import cv2 as cv 
import numpy as np 

drawing = False
mode = True

(ix,iy) = (-1,-1)

window = 'Drawing'
cv.namedWindow(window)
img = np.zeros ((900,900,3),np.uint8)

def draw (event,x,y,flags,param):
    global drawing , mode , ix , iy

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True 
        (ix,iy) = x,y 
    
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True :
            if mode == True :
                cv.rectangle (img,(ix,iy),(x,y),(8,102,255),-1)
            else :
                cv.circle (img, (x,y),4,(0,255,0),-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False 



cv.setMouseCallback(window,draw)


def main ():
    global mode 
    while True :
        cv.imshow (window,img)
        k = cv.waitKey(1)
        if k == ord ('m') or k == ord ('M'):
            mode = not mode 
        elif k == 27:
            break

    
    cv.destroyAllwindows()

main()