import cv2
import numpy as np
from matplotlib import pyplot as plt

file_path = 'professor.jpg'
dest_path = 'professor_edge.jpg'

img = cv2.imread(file_path,0)
edges = cv2.Canny(img,50,100,False)
cv2.imwrite(dest_path, edges)
