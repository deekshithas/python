'''import cv2
img=cv2.imread("pix.jpg")
cv2.imshow("hello world",img)
cv2.waitKey(0)
print(img.shape)

print("height of the image:",int(img.shape[0]),"pixels")
print("width of the image:",int(img.shape[1]),"pixels")
cv2.imwrite("output.jpg",img)
cv2.imwrite("output.png",img)

cv2.destroyAllWindows()
'''
#import cv2
#gray scale image
'''img=cv2.imread("pix.jpg")
cv2.imshow("original",img)
cv2.waitKey(0)

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayscale",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#binary image

'''img=cv2.imread("pix.jpg",0)
ret,th=cv2.threshold(img,125,255,cv2.THRESH_BINARY)
print(ret)
ret,th1=cv2.threshold(img,125,255,cv2.THRESH_BINARY_INV)
cv2.imshow("hello world",img)
cv2.imshow("hello world",th)
cv2.imshow("hello world",th1)
cv2.waitKey(0)

cv2.destroyAllWindows()'''

'''img=cv2.imread("pix.jpg")
B,G,R=img[0,0]
print(B,G,R)
print(img.shape)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(gray.shape)
print(gray[0,0])
ret,th=cv2.threshold(gray,125,255,cv2,THRESH_BINARY)
print(th.shape)
print(th[0,0])'''


'''img=cv2.imread("pix.jpg")
img_HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV image",img_HSV)
cv2.imshow("hue channel",img_HSV[:,:,0])
cv2.imshow("saturation",img_HSV[:,:,1])
cv2.imshow("value channel",img_HSV[:,:,2])
cv2.waitKey(0)
cv2.destroyAllWindows()'''

'''#create a black images
import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
cv2.imshow("black rectangle (color)",img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#create a white images

import cv2
import numpy as np
img=np.ones((512,512,3),np.uint8)*255
cv2.imshow("white rectangle (color)",img)
cv2.waitKey(0)
cv2.destroyAllWindows()





































