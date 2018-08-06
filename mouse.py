# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np


def ImageSubtracr(img, objimg):
    cv.imshow("output", objimg)
    element = cv.getStructuringElement(cv.MORPH_RECT, (2, 2))
    cv.morphologyEx(objimg, objimg, cv.MORPH_ERODE, element)
    element = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    cv.morphologyEx(objimg, objimg, cv.MORPH_DILATE, element)
    cv.imshow("res1", objimg)
    dstimg = img - objimg
    cv.imshow("res2", dstimg)
    cv.waitKey(0)


def Inpainting(img, maskimg):
    element = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))
    cv.dilate(maskimg, maskimg, element)
    # cv.cvtColor(maskimg, grayMask, cv.COLOR_BGR2GRAY, 1)
    cv.inpaint(img, grayMask, inpain, 3, cv.INPAINT_TELEA)
    cv.imshow('r', Inpainting)


def GetRed(srcimg):
    dstimg = srcimg[:, :, 2]
    return dstimg


def GetGreen(srcImg):
    dstImg = srcImg[:, :, 1]
    return dstImg


def GetBlue(srcImg):
    dstImg = srcImg[:, :, 0];
    return dstImg


color = [([0, 0, 190], [100, 100, 225])]


def GetRedComponet(srcImg):
    dstImg = srcImg
    for (l, u) in color:
        l = np.array(l)
        u = np.array(u)
        mask = cv.inRange(dstImg, l, u)
        dstImg = cv.bitwise_and(dstImg, dstImg, mask=mask)
    cv.imshow('r', dstImg)
    return dstImg


if __name__ == '__main__':
    srcimg = cv.imread('images/mm2.jpg')
    cv.imshow('w', srcimg)
    imgcomponet = GetRedComponet(srcimg)
    Inpainting(srcimg, imgcomponet)
    cv.waitKey(0)
