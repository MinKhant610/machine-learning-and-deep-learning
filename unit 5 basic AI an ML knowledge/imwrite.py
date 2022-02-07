import cv2 as cv 
img1 = cv.imread ('images/min.jpg',1)
img2 = cv.imread ('images/min.jpg',0)
img3 = cv.imread ('images/min.jpg',-1)

cv.imshow ('Linux_color',img1)
cv.imshow ('Linux_gray',img2)
cv.imshow ('Linux_no_change',img3)

cv.imwrite ('linux_grey.jpg',img2)
cv.waitKey (0)
cv.destroyAllWindow