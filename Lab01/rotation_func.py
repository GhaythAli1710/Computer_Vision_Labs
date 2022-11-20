import math

import cv2 as cv
import numpy as np

image = cv.imread('img1.jpg')
rows, cols, _ = image.shape
print("height : " + str(rows))
print("width : " + str(cols))
angle = 90
center_x = cols / 2
center_y = rows / 2

# /**** _1_ ****/
theta = angle / 180 * np.pi
alpha = math.cos(theta)
peta = math.sin(theta)

tx = (1 - alpha) * center_x - peta * center_y
ty = peta * center_x + (1 - alpha) * center_y

M = np.float32([
    [alpha, peta, tx],
    [-peta, alpha, ty]
])

# M = np.float32([
#     [alpha, -peta],
#     [peta, alpha]
# ])

# /**** _2_ ****/
# M = cv.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)

# /**** _advanced_ ****/
# 1  2
# 3  4   ===>   1  3  5
# 5  6   ===>   2  4  6
# dst = cv.transpose(image)

# /**** _advanced2_ ****/
# 1  2  3           3  2  1
# 4  5  6   ====>   6  5  4
# 7  8  9           9  8  7
# dst = cv.flip(image, 0)
# dst = cv.flip(image, 1)
# dst = cv.flip(image, -1)

# /**** _extra_ ****/
# dst = cv.rotate(image, cv.ROTATE_90_CLOCKWISE)
# dst = cv.rotate(image, cv.ROTATE_90_COUNTERCLOCKWISE)
# dst = cv.rotate(image, cv.ROTATE_180)

# print(M)
# dst = cv.warpAffine(image, M, (cols, rows))
# print("height : " + str(dst.shape[0]))
# print("width : " + str(dst.shape[1]))
cv.imshow('dst', dst)

k = cv.waitKey(0)
if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite("translation.png", dst)
    cv.destroyAllWindows()
