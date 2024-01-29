import cv2
import numpy as np

image = cv2.imread('banana.jpg')
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

L, A, B = cv2.split(lab_image)
print(f"{np.min(L) = } - {np.max(L) = } - {L.dtype}") # uint8
print(f"{np.min(A) = } - {np.max(A) = } - {A.dtype}") # uint8
print(f"{np.min(B) = } - {np.max(B) = } - {B.dtype}") # uint8
L = cv2.add(L, 100) # max = 255
A = cv2.add(A, 1000) # max = 255
B = cv2.subtract(B, 5000) # min = 0

modified_lab_image = cv2.merge([L, A, B])
modified_rgb_image = cv2.cvtColor(modified_lab_image, cv2.COLOR_LAB2BGR)

cv2.imshow('Original Image', image)
cv2.imshow('Modified Image', modified_rgb_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
