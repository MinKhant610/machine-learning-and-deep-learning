import cv2 as cv 

def main():
    img1 = cv.imread ('images/min.jpg',1)
    img2 = cv.imread ('images/min.jpg',0)

    print (type(img1))
    print (img1.dtype)
    print (img1.shape)
    print (img1.ndim)
    print (img2.ndim)

if __name__ == '__main__':
    main()