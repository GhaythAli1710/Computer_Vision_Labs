import cv2 as cv
import numpy as np

image = cv.imread('img1.jpg')
(rows, columns) = image.shape[:2]
print("height : " + str(rows))
print("width : " + str(columns))

tx = -50
ty = -50
M = np.float32([
    [1, 0, tx],
    [0, 1, ty]
])

dst = cv.warpAffine(image, M, (columns + tx, rows + ty))
print("height : " + str(dst.shape[0]))
print("width : " + str(dst.shape[1]))
cv.imshow("img", dst)

k = cv.waitKey(0)
if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite("translation.png", dst)
    cv.destroyAllWindows()
