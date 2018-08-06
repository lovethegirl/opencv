# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np


class openvideo:
    def readcap(self, path):
        img = cv.imread(path)
        print(img)
        cv.namedWindow("Image")
        cv.imshow("Image", img)
        ch = cv.waitKey(3000)
        cv.destroyAllWindows()
        cap = cv.VideoCapture(0)
        while(cap.isOpened()):
            ret, frame = cap.read()
            # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            cv.imshow('frame', frame)
            if cv.waitKey(25) & 0xFF == ord('q'):
                break
        cap.release()
        cv.destroyAllWindows()

    def savefile(self, name):
        cap = cv.VideoCapture(0)
        fourcc = cv.VideoWriter_fourcc(*'H264')
        out = cv.VideoWriter(name, fourcc, 20.0, (640, 480))
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                # frame = cv.flip(frame, 0)
                out.write(frame)
                cv.imshow('frame', frame)
                if cv.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        out.release()
        cv.destroyWindow()

    def playvideo(self, name):
        cap = cv.VideoCapture(name)
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                cv.imshow('frame', gray)
                if(cv.waitKey(35) & 0xFF == ord('q')):
                    break
            else:
                break
        cap.release()
        # cv.destroyWindow()


if __name__ == '__main__':
    work = openvideo()
    # work.savefile('video/out.avi')
    # work.playvideo('../video/1.mp4')
    work.readcap('../images/1.jpg')
