
import cv2
import numpy as np

im = cv2.imread('flower.jpg')
#change the color BGR to HSV
gray = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

cv2.imshow('hello worldpytho', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

