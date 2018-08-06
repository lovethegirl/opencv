import cv2 as cv
import os
import time


class face:
    def savevideo(self, name):
        cap = cv.VideoCapture(0)
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        out = cv.VideoWriter(name, fourcc, 20.0, (640, 480))
        cv.namedWindow('frame')
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
        # cv.destroyAllWindow()

    def readface(self):
        cap = cv.VideoCapture(0)
        cv.namedWindow('face')
        face = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
        while(cap.isOpened()):
            ret, frame = cap.read()
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            faces = face.detectMultiScale(
                gray, scaleFactor=1.15, minNeighbors=5)
            print("find {0} face".format(len(faces)))
            for(x, y, w, h) in faces:
                cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
            cv.imshow('face', frame)
            if cv.waitKey(1) & 0xFF == 27:
                break
        cap.release()
        cv.destroyAllWindows()

    def playvideo(self, inpath, outpath):
        count = 0
        cap = cv.VideoCapture(inpath)
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                count += 1
                cv.imshow('frame', frame)
                if(cv.waitKey(35) & 0xFF == ord('q')):
                    break
                if count % 30 == 0:
                    cv.imwrite(outpath + str(count / 30) + '.jpg', frame)
            else:
                break
        cap.release()
        cv.destroyAllWindows()

    def writeface(self, inpath, outpath):
        face = cv.CascadeClassifier(r'haarcascade_frontalface_default.xml')
        frame = cv.imread(inpath)
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray, scaleFactor=1.20, minNeighbors=10)
        for(x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
        print("find {0} face".format(len(faces)))
        cv.imwrite(outpath, frame)
        cv.imshow('find', frame)
        cv.waitKey(delay=500)


if __name__ == '__main__':
    f = face()
    # f.readface()
    # f.savevideo('../video/out.avi')
    f.playvideo('../video/out.avi', '../images/')
    DIR = '../images'
    length = len([name for name in os.listdir(DIR)
                  if os.path.isfile(os.path.join(DIR, name))])
    print(length)
    for i in range(1, length + 1):
        print(i)
        f.writeface('../images/' + str(i) + '.jpg',
                    '../newpic/' + str(i) + '.jpg')
