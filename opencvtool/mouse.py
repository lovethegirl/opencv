# -*- coding: utf-8 -*-

import cv2
import numpy as np

# 当鼠标按下时变为True
drawing = False
# 如果mode为true绘制矩形。按下'm' 变成绘制曲线。
mode = True
ix, iy = -1, -1

# 创建回调函数


def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode

    # 当按下左键是返回起始位置坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)
        drawing == False


mode = 1
x1, y1, x2, y2 = -1, -1, -1, -1


def onmouseaction(event, x, y, flags, param):
    global x1, y1, x2, y2
    if mode == 0 and event == cv2.EVENT_LBUTTONDOWN:
        print('l_c')
        # cv2.line(img, (0, 0), (x, y), (255, 255, 0), 2)
        x1, y1 = x, y
    elif mode == 0 and event == cv2.EVENT_LBUTTONUP:
        cv2.line(img, (x1, y1), (x, y), (0, 0, 255), 2)
    elif mode == 1 and event == cv2.EVENT_LBUTTONDOWN:
        x2, y2 = x, y
    elif mode == 1 and event == cv2.EVENT_LBUTTONUP:
        print('l_l')
        cv2.rectangle(img, (x2, y2), (x, y), (0, 255, 0), 2)


if __name__ == '__main__':
    # img = cv2.imread('images/2.jpg')
    # cv2.namedWindow('image')
    # # 绑定事件
    # cv2.setMouseCallback('image', draw_circle)
    # while(1):
    #     cv2.imshow('image', img)
    #     k = cv2.waitKey(1) & 0xFF
    #     if k == ord('m'):
    #         mode = not mode
    #     elif k == 27:
    #         break
    #img = np.zeros((500, 500, 3), np.uint8)
    img = cv2.imread('../images/mm1.jpg')
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', onmouseaction)
    while(1):
        cv2.imshow("image", img)
        c = cv2.waitKey(1)
        if c == ord('l'):
            mode = 0
        elif c == ord('r'):
            mode = 1
        elif c == 27:
            break
    cv2.imwrite('images/mm2.jpg', img)
    cv2.destroyAllWindows()
