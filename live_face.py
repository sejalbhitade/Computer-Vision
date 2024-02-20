import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(0)

while cap.isOpened():
    ret,img=cap.read()

    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray_img,scaleFactor=1.1, minNeighbors = 3)

    for x,y,w,h in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyA11Windows()