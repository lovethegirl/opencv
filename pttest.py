from pycls.opecv_video import openvideo
from biaozhu.biaozhu import fea
from biaozhu.videoface import face
import os
import cv2 as cv
import time


def savevideo(name):
    cap = cv.VideoCapture(0)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter(name, fourcc, 20.0, (640, 480))
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            out.write(frame)
            cv.imshow('frame', frame)
            if cv.waitKey(20) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv.destroyAllWindow()


def readface():
    cap = cv.VideoCapture(0)
    cv.namedWindow('face')
    while(cap.isOpened()):
        face = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
        ret, frame = cap.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5)
        print('find {0} face'.format(len(faces)))
        for(x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
        cv.imshow('face', frame)
        if cv.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()


def playvideo(name):
    count = 0
    cap = cv.VideoCapture(name)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            count += 1
            cv.imshow('frame', frame)
            if(cv.waitKey(35) & 0xFF == 27):
                break
            if count % 30 == 0:
                cv.imwrite('images/' + str(count / 30) + '.jpg', frame)
        else:
            break
    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    f = face()
    f.readface()
