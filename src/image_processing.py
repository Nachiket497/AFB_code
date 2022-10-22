import numpy as np
import cv2


# take the input image and threshold the green pixels
def green_threshold(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_green = np.array([25, 0, 0])
    upper_green = np.array([86, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    return mask

# avg filter to smooth out the image


def avg_filter(img):
    kernel = (1/10)*np.array([
        [0, 0.5, 1, 0.5, 0],
        [0.5, 1, 1, 1, 0.5],
        [1, 1, 1, 1, 1],
        [0.5, 1, 1, 1, 0.5],
        [0, 0.5, 1, 0.5, 0]
    ])
    dst = cv2.filter2D(img, -1, kernel)
    return dst

# single value thresholding


def single_value_threshold(img):
    ret, thresh1 = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)
    return thresh1

# take min in the window from the image


def min_filter(img):
    kernel = np.ones(shape=(5, 5), dtype=np.uint8)
    dst = cv2.erode(img, kernel, iterations=1)
    return dst

# vertical interpolation


def vertical_interpolation(img):
    dst = cv2.resize(img, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
    return dst

# interpolation nearest neighbour


def nearest_neighbour(img):
    dst = cv2.resize(img, None, fx=1, fy=1, interpolation=cv2.INTER_NEAREST)
    return dst

# morphological operations dilation if m nor wrong


def dilation(img):
    kernel = np.ones(shape=(5, 5), dtype=np.uint8)
    dst = cv2.dilate(img, kernel, iterations=1)
    return dst


def erosion(img):
    kernel = np.ones(shape=(5, 5), dtype=np.uint8)
    dst = cv2.erode(img, kernel, iterations=1)
    return dst

# draw a red pixel at the avg position of white pixels in each row


def draw_line(img):
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    for i in range(img.shape[0]):
        white_pixels = np.where(img[i, :, 0] == 255)
        if len(white_pixels[0]) > 0:
            avg = int(np.mean(white_pixels))
            img[i, avg, :] = [0, 0, 255]
    return img


if __name__ == '__main__':
    # read the image
    img = cv2.imread('test.png')
    # threshold the image
    mask = green_threshold(img)
    for _ in range(3):
        # mask = nearest_neighbour(mask)
        mask = avg_filter(mask)
        mask = single_value_threshold(mask)
        mask = dilation(mask)
        mask = erosion(mask)

    mask = erosion(mask)
    mask = erosion(mask)
    mask = erosion(mask)
    mask = dilation(mask)
    mask = erosion(mask)
    mask = dilation(mask)
    mask = erosion(mask)
    mask = dilation(mask)
    mask = min_filter(mask)
    mask = dilation(mask)

    for _ in range(3):
        # mask = nearest_neighbour(mask)
        mask = avg_filter(mask)
        mask = single_value_threshold(mask)
        mask = dilation(mask)
        mask = erosion(mask)

    # mask = mirror_image(mask)
    mask = single_value_threshold(mask)
    mask = dilation(mask)
    mask = draw_line(mask)
    # mask = draw_st_line(mask)
    try:  # show the images
        cv2.imshow('image', img)
        cv2.imshow('mask', mask)
        cv2.waitKey(5000)
    except KeyboardInterrupt:
        cv2.destroyAllWindows()
