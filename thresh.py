import cv2
img=cv2.imread('zebra.jpg')
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh_img=cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY)

cv2.imshow('img',img_gray)
cv2.imshow('ithresh_imges',thresh_img)
cv2.waitKey(0)
cv2.destroyA11Windows()
