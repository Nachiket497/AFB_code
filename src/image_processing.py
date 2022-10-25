import numpy as np
import cv2


# take the input image and threshold the green pixels
def green_threshold(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_green = np.array([25, 0, 0])
    upper_green = np.array([86, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    return mask


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


def single_value_threshold(img, cutoff=65):
    ret, thresh1 = cv2.threshold(img, cutoff, 255, cv2.THRESH_BINARY)
    return thresh1


def min_filter(img):
    kernel = np.ones(shape=(3, 3), dtype=np.uint8)
    dst = cv2.erode(img, kernel, iterations=1)
    return dst


def nearest_neighbour(img):
    dst = cv2.resize(img, None, fx=1, fy=1, interpolation=cv2.INTER_NEAREST)
    return dst


def dilation(img):
    kernel = np.ones(shape=(5, 5), dtype=np.uint8)
    dst = cv2.dilate(img, kernel, iterations=1)
    return dst


def opening(img):
    kernel = np.ones(shape=(5, 5), dtype=np.uint8)
    dst = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    return dst


def avg_white(img):
    x, y = [], []
    for i in range(len(img)):
        for j in range(len(img[0])):
            if img[i][j] == 255:
                x.append(i)
                y.append(j)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    x, y = sum(x)//len(x), sum(y)//len(y)
    img = draw_stline(img, x, y, [255, 0, 0])
    return img, x, y


def divide_avg(img):
    x, y = img.shape
    posx, posy = [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]
    img_new = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    img_new[:x//3, :(y//2)], posx[0], posy[0] = avg_white(img[:x//3, :(y//2)])
    img_new[:x//3, y//2:], posx[1], posy[1] = avg_white(img[:x//3, y//2:])
    img_new[x//3:2*x//3, :y //
            2], posx[2], posy[2] = avg_white(img[x//3:2*x//3, :y//2])
    img_new[x//3:2*x//3, y //
            2:], posx[3], posy[3] = avg_white(img[x//3:2*x//3, y//2:])
    img_new[2*x//3:, :y//2], posx[4], posy[4] = avg_white(img[2*x//3:, :y//2])
    img_new[2*x//3:, y//2:], posx[5], posy[5] = avg_white(img[2*x//3:, y//2:])

    posx[2] += x//3
    posx[3] += x//3
    posx[4] += 2*x//3
    posx[5] += 2*x//3
    posy[1] += y//2
    posy[3] += y//2
    posy[5] += y//2

    return img_new, [posx, posy]


def draw_stline(img, posx, posy, color1=[0, 0, 255]):
    for i in range(len(img)):
        img[i, posy] = color1
    return img


def process_image(img):
    mask = green_threshold(img)
    for _ in range(5):
        mask = nearest_neighbour(mask)
        mask = min_filter(mask)
        mask = avg_filter(mask)
        mask = single_value_threshold(mask)
        mask = opening(mask)
    mask = dilation(mask)
    mask = dilation(mask)
    mask = opening(mask)
    mask = avg_filter(mask)
    mask = single_value_threshold(mask, 100)

    # mask = avg_white(mask)
    mask, pos = divide_avg(mask)
    mask = draw_stline(mask, sum(pos[0][2:4])//2, sum(pos[1][2:4])//2)
    mask = draw_stline(mask, sum(pos[0][4:6])//2, len(mask[0])//2, [0, 255, 0])

    return mask, sum(pos[1][2:4])//2 - len(mask[0])//2


if __name__ == "__main__":

    img = cv2.imread('test.png')
    mask, error = process_image(img)

    try:  # show the images
        cv2.imshow('image', img)
        cv2.imshow('mask', mask)
        cv2.waitKey(10000)
    except KeyboardInterrupt:
        cv2.destroyAllWindows()
