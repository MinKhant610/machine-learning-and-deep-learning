import cv2 as cv 
import numpy as np 

window = 'Drawing'
cv.namedWindow(window)
img = np.zeros ((512,512,3),np.uint8)

def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),40,(0,255,0),1)
    elif event == cv.EVENT_MBUTTONDOWN:
        cv.circle(img,(x,y),20,(255,0,0),-1)


cv.setMouseCallback(window,draw_circle)


def main ():
    while True :
        cv.imshow (window,img)
        if cv.waitKey(20) == 27:
            break 
    cv.destroyAllwindows()

main()