import cv2 as cv
import numpy as np


def CamGui():
    capture = cv.VideoCapture(0)
    width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
    prev_gray = cv.CreateImage((width, height), 8, 1)
    gray = cv.CreateImage((width, height), 8, 1)

    # Will hold the pyr frame at t-1
    prevPyr = cv.CreateImage((height / 3, width + 8), 8, cv.CV_8UC1)
    currPyr = cv.CreateImage((height / 3, width + 8),
                             8, cv.CV_8UC1)  # idem at t

    max_count = 500
    qLevel = 0.01
    minDist = 10
    prev_points = []  # Points at t-1
    curr_points = []  # Points at t
    lines = []  # To keep all the lines overtime

    while True:
        frame = cv.QueryFrame(capture)
        cv.CvtColor(frame, gray, cv.CV_BGR2GRAY)  # Convert to gray
        output = cv.CloneImage(frame)

        prev_points = cv.GoodFeaturesToTrack(
            gray, None, None, max_count, qLevel, minDist)
        curr_points, status, err = cv.CalcOpticalFlowPyrLK(
            prev_gray, gray, prevPyr, currPyr, prev_points, (10, 10), 3, (cv.CV_TERMCRIT_ITER | cv.CV_TERMCRIT_EPS, 20, 0.03), 0)

        # If points status are ok and distance not negligible keep the point
        k = 0
        for i in range(len(curr_points)):
            nb = abs(int(prev_points[i][0]) - int(curr_points[i][0])) + \
                abs(int(prev_points[i][1]) - int(curr_points[i][1]))
            if status[i] and nb > 2:
                prev_points[k] = prev_points[i]
                curr_points[k] = curr_points[i]
                k += 1

        prev_points = prev_points[:k]
        curr_points = curr_points[:k]
        # At the end only interesting points are kept

        # Draw all the previously kept lines otherwise they would be lost the next frame
        for (pt1, pt2) in lines:
            cv.Line(frame, pt1, pt2, (255, 255, 255))

        # Draw the lines between each points at t-1 and t
        for prevpoint, point in zip(prev_points, curr_points):
            prevpoint = (int(prevpoint[0]), int(prevpoint[1]))
            cv.Circle(frame, prevpoint, 15, 0)
            point = (int(point[0]), int(point[1]))
            cv.Circle(frame, point, 3, 255)
            cv.Line(frame, prevpoint, point, (255, 255, 255))
            # Append current lines to the lines list
            lines.append((prevpoint, point))

        cv.Copy(gray, prev_gray)  # Put the current frame prev_gray
        prev_points = curr_points

        cv.ShowImage("The Video", frame)
        #cv.WriteFrame(writer, frame)
        c = cv.WaitKey(1)
        if c == 27:  # Esc on Windows
            break


if __name__ == '__main__':
    CamGui()
