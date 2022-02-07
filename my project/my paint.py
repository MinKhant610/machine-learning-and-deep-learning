import numpy as np 
import cv2 as cv

window = 'Circle and Rectangle'
cv.namedWindow (window)
img = np.zeros ((512,512,3),np.uint8)
text = 'Developed by Min Khant'
cv.putText (img,text,(0,50),cv.FONT_HERSHEY_SIMPLEX,1,(197,0,166))

(ix,iy) = (-1,-1)
drawing = True
mode = True

def draw (event,x,y,flags,param):
    global mode,drawing ,ix,iy

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = False 
        (ix,iy) = x,y


    elif event == cv.EVENT_LBUTTONDBLCLK :
        cv.circle (img,(x,y),40,(0,255,255),1)

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == False:
            if mode == True:
                cv.rectangle (img,(ix,iy),(x,y),(255,0,0),-1)
            else :
                cv.circle (img,(x,y),4,(0,0,190),-1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = True

cv.setMouseCallback (window,draw)

def main ():

    global mode 

    while True :
        cv.imshow (window,img)

        k = cv.waitKey (1)

        if k == ord ('m') or k == ord ('M'):
            mode = not mode

        elif k == 27 :
            break

    cv.destroyAllwindows ()

main()

