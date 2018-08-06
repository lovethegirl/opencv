import cv2 as cv


class fea:
    def __init__(self, path):
        self.path = path

    def writerec(self, l_col, l_row, r_col, r_row):
        # frame = self.path
        # self.img = cv.imread(frame)
        cv.rectangle(self.img, (l_col, l_row),
                     (r_col, r_row), (0, 255, 0), 4)

    def writetext(self, text, col, row):
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(self.img, text, (col, row), font, 2, (0, 0, 225), 1)

    def save(self, path):
        cv.imwrite(path, self.img)

    def findface(self, path):
        face = cv.CascadeClassifier(r'haarcascade_frontalface_default.xml')
        self.img = cv.imread(self.path)
        gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5)
        print("find {0} face".format(len(faces)))
        for(x, y, w, h) in faces:
            self.writerec(x, y, x + w, y + h)
        self.save(path)
        cv.imshow('find', self.img)
        cv.waitKey(delay=500)


if __name__ == '__main__':
    f = fea('../images/2.jpg')
    f.findface('../newpic/2.jpg')
