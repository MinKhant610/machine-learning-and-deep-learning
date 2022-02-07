import cv2
import numpy as np

drawing = False # true if mouse is pressed
mode = True 
ix, iy = -1, -1

def nothing(x):
    pass

cv2.namedWindow('Controls', cv2.WINDOW_NORMAL)  #--- window to have all the controls

cv2.createTrackbar("R", "Controls", 0, 255, nothing)
cv2.createTrackbar("G", "Controls", 0, 255, nothing)
cv2.createTrackbar("B", "Controls", 0, 255, nothing)

cv2.createTrackbar("Paint brush thickness", "Controls",0, 30, nothing)

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img, (x, y), pb_thick, (r, g, b), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img, (x, y), pb_thick, (r, g, b), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image',img)

    r = cv2.getTrackbarPos("R", "Controls")
    g = cv2.getTrackbarPos("G", "Controls")
    b = cv2.getTrackbarPos("B", "Controls")

    pb_thick = cv2.getTrackbarPos("Paint brush thickness", "Controls")

    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()