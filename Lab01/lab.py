import cv2 as cv
import numpy as np

image = cv.imread('img1.jpg')

# /*** gray image ***/
# image = cv.imread('img1.jpg', 0)

# cv.imshow("image", image)

# print(image.shape)
# print(image.size)
# print(image.dtype)

# b, g, r = cv.split(image)

# cv.imshow("blue", b)
# cv.imshow("blue", [:,:,1])
# print(b.dtype)
# print(b.shape)

# print(g.dtype)
# print(g.shape)

# img = cv.merge((b, g, r))
# cv.imshow("img", img)

# HSV = cv.cvtColor(image, cv.COLOR_BGR2HSV)
# GRAY = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# RGB = cv.cvtColor(GRAY, cv.COLOR_GRAY2RGB)
# cv.imshow("img", RGB)

# dim = image.shape
# print(dim)
# print(dim[0])
# print(dim[1])
#
# res = cv.resize(image, (int(dim[1]/2), int(dim[0]/2)))
# cv.imshow("img", res)

# (rows, columns) = image.shape[:2]
# M = np.float32([[1, 0, 100],
#                 [0, 1, 50]])
# dst = cv.warpAffine(image, M, (columns, rows))
# cv.imshow("img", dst)

rows, cols, _ = image.shape
M = cv.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
dst = cv.warpAffine(image, M, (cols, rows))
cv.imshow('dst', dst)

k = cv.waitKey(0)
if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite("translation.png", dst)
    cv.destroyAllWindows()
