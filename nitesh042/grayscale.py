import numpy as np
import cv2 

image=cv2.imread('scenes.jpg')

src = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
filename = 'gray.jpg'
cv2.imwrite(filename,src)
