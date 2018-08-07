#-*- coding:utf-8 -*-
import cv2 as cv
import numpy as np
f_capture_update = False
g_currentframe = 0

ix, iy = -1, -1
drawing = False
frame = -1


def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing

    # 当按下左键是返回起始位置坐标
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_LBUTTONUP:
        cv.rectangle(frame, (ix, iy), (x, y), (0, 255, 0), 4)
        drawing == False


def on_Trackbar(event):
    if event == cv.EVENT_FLAG_LBUTTON:
        print "a"
        global g_currentframe
        f_capture_update = True
        g_currentframe += 20


def ImageText(image, text, x, y):
    cv.putText(image, text, (x, y), cv.FONT_HERSHEY_PLAIN,
               1, (255, 255, 255), 1)


def videoplayer(path):
    # cv.setMouseCallback('')
    global g_currentframe
    trackname = 'play'
    windwos = 'video'
    cv.setMouseCallback(windwos, draw_circle)
    delay_ms = 35
    f_stop = False
    f_nextstop = False
    f_perframe = False
    f_capture_update = False
    f_pause = False
    cap = cv.VideoCapture(path)
    totalframe = cap.get(7)
    cv.namedWindow(windwos)
    g_currentpercnet = 0
    cv.createTrackbar(trackname, windwos,
                      0, 100, on_Trackbar)
    # on_Trackbar(g_currentframe)
    global ret, frame
    while(f_stop == False):
        if not f_pause:
            ret, frame = cap.read()
            if ret == True:
                cv.imshow(windwos, frame)
            else:
                break
            if f_capture_update == True:
                setframe = g_currentpercnet * totalframe / 100
                g_currentframe = setframe
                print(g_currentframe)
                f_capture_update = False
            g_currentframe = g_currentframe + 1
            g_currentpercnet = int(g_currentframe * 100 / totalframe)
            cv.setTrackbarPos(trackname, windwos, g_currentpercnet)
            if g_currentpercnet == 100:
                g_currentframe = 0
                # g_currentpercnet=0
                g_currentframe += 1
                cap.set(1, g_currentframe)
        ch = cv.waitKey(delay_ms) & 0xFF
        if ch == 27:
            f_stop = True
        elif ch == ord('u'):
            delay_ms = 10
        elif ch == ord('i'):
            delay_ms = 35
        elif ch == ord('o'):
            delay_ms = 100
        elif ch == ord(' '):
            f_pause = not f_pause

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    print('start video')
    videoplayer('../video/out.avi')
