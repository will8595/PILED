#!/usr/bin/env python

from effects import *
x = 0.5
y = input("Times Thru: ")
for i in range(y):
    red(x)
    red(x, 100)
    orange(x)
    orange(x, 100)
    yellow(x)
    yellow(x, 100)
    green(x)
    green(x, 100)
    blue(x)
    blue(x, 100)
    purple(x)
    purple(x, 100)
    blueSoftBuild(.01, 3)
    kill(.2)
    strobeWhite(1, 0.05)
    rgbCrossFade(0.0075, 8, 2)
    kill(.2)
    for i in range(3):
        redSoftBuild(0.01, 3)
        strobeRed(1, 0.05)
        greenSoftBuild(0.01, 3)
        strobeGreen(1, 0.05)
        blueSoftBuild(0.01, 3)
        strobeBlue(1, 0.05)
    whiteSoftFade(0.01, 3)
    rgbSoftFade(0.005475, 30, 4)

kill()
