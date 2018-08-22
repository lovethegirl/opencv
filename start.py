import numpy as np
import cv2 as cv
# mouse callback function
img = np.zeros((300, 512, 3), np.uint8)
drawing = False  # true if mouse is pressed
mode = True  # if True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1

# def draw_circle(event, x, y, flags, param):
#     if event == cv.EVENT_LBUTTONDBLCLK:
#         cv.circle(img, (x, y), 100, (255, 0, 0), -1)


# Create a black image, a window and bind the function to window
# mouse callback function
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode, img
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv.circle(img, (x, y), 5, (0, 0, 255), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        # if mode == True:
        #     cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)01
        # else:
        #     cv.circle(img, (x, y), 5, (0, 0, 255), -1)


def mouse_circle():
    global imgs
    cv.namedWindow('image')
    cv.setMouseCallback('image', draw_circle)
    global mode
    while(1):
        cv.imshow('image', img)
        k = cv.waitKey(20) & 0xFF
        if k == ord('m'):
            mode = not mode
        elif k == 27:
            break
    cv.destroyAllWindows()


def nothing(x):
    pass


def trackbar():
    # img = no.zeros((300, 512, 3), np.uint8)
    cv.namedWindow("image")
    cv.createTrackbar('R', 'image', 0, 255, nothing)
    cv.createTrackbar('G', 'image', 0, 255, nothing)
    cv.createTrackbar('B', 'image', 0, 255, nothing)
    switch = '0:OFF\n1:ON'
    cv.createTrackbar(switch, 'image', 0, 1, nothing)
    while(1):
        cv.imshow('image', img)
        k = cv.waitKey(delay=25) & 0xFF
        if k == 27:
            break
        r = cv.getTrackbarPos('R', 'image')
        g = cv.getTrackbarPos('G', 'image')
        b = cv.getTrackbarPos('B', 'image')
        s = cv.getTrackbarPos(switch, 'image')
        if s == 0:
            img[:] = 0
        else:
            img[:] = [b, g, r]


if __name__ == '__main__':
    # mouse_circle()
    trackbar()
