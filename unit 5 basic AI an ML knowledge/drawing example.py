import cv2 as cv
import numpy as np 

def main():
    img = np.zeros ((512,512,3) , np.uint8)
    cv.rectangle (img,(40,60),(80,100),(0,255,0),2)
    cv.circle (img , (150,150),20,(0,0,255),1)
    cv.ellipse (img , (200,200),(50,20),0,0,360,(250,0,0),-1)

    points = np.array ([[67,88],[80,90],[99,55]])
    print (points)
    cv.polylines (img,[points],True,(0,255,0))

    text = 'Testing Computer Drawing'
    cv.putText (img,text,(10,404),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255))
    
    cv.imshow ('Black',img)
    cv.waitKey (0)
    cv.destroyAllWindow()

if __name__ == '__main__':
    main()