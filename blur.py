import cv2
img=cv2.imread('zebra.jpg')

img_blur=cv2.blur(img,(7,7))

def resize_img(img,scale):

    h=img.shape[0]
    w=img.shape[1]

    new_h=int(h*scale)
    new_w=int(w*scale)
    return cv2.resize(img,(new_w,new_h))

img_res=resize_img(img,0.40)

img_blur=cv2.blur(img_res,(7,7))
img_G_blur=cv2.GaussianBlur(img_res,(7,7),3)
img_m_blur=cv2.medianBlur(img_res,7)


cv2.imshow('img',img)

cv2.imshow('img_res',img_blur)
cv2.imshow('img__G_blur',img_G_blur)
cv2.imshow('img_blur',img_blur)
cv2.imshow('img_m_blur',img_m_blur)
cv2.waitKey(0)
cv2.destroyA11Windows()
