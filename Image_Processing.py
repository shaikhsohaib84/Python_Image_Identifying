import cv2
#open an image
#img = cv2.imread("F:\mine\white.jpg",1)

#resize an image
#resized = cv2.resize(img,(int(img.shape[1]/2), (int(img.shape[0]/2))));

#display an image
#cv2.imshow("pic",resized);
#for(0ms)if any key is press, then window will terminate
#cv2.waitKey(0)
#close window
#cv2.destroyAllWindows()


#create a cascadeclassifier object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#reading the image as it is
img = cv2.imread("F:\mine\IMG-20200114-WA0014.jpg")

#reading the image in gray scale image
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#search the co-ordinates of the image
faces = face_cascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=5)

for x,y,w,h in faces:
    img = cv2.rectangle(img ,(x,y), (x+w,y+h), (0,255,0), 3)

cv2.imshow("gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()