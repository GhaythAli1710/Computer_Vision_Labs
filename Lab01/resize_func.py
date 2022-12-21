import cv2 as cv


# first Rule
def resize(image, height=None, width=None):
    if height is None and width is None:
        return image

    (h, w) = image.shape[:2]
    dimension = None

    if height is not None:
        ratio = height / float(h)
        dimension = (int(w * ratio), height)

    elif width is not None:
        ratio = width / float(w)
        dimension = (width, int(h * ratio))

    return cv.resize(image, dimension)


# aspect ratio function
def aspect_ratio(height, width):
    return width / height


# test rule
img = cv.imread('img1.jpg')
height = img.shape[0]  # rows_num
width = img.shape[1]  # columns_num

print(f" image shape is : " + str(img.shape))
print(f" dimension image = [ height = " + str(height) + " , width = " + str(width) + " ]")
print(f" aspect ratio = " + str(aspect_ratio(height, width)))

test = resize(img, height=600)
print(str(aspect_ratio(test.shape[0], test.shape[1])))
cv.imshow("img", test)
cv.waitKey(0)
