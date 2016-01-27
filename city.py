#!/usr/bin/env/ python
import time
import effects
when = input("Current 24 hr time: ")
hr = int(str(when)[:2])
min = int(str(when)[-2:])
hr *= 3600
min *= 60
when = hr + min
print(hr, min, when)
length = input("How long in minutes? ")
length *= 60
start = time.time()
end = time.time()
firstRun = True
diff1 = time.time()
diff2 = time.time()
while (end - start) < length:
    if firstRun:
        diff = 0
        firstRun = False
    else:
        diff = diff2 - diff1
    diff1 = time.time()    
    when += diff
    print(start, end, when, diff1, diff2, diff)
    if when <= 14400:
        r = 75
        g = 10
        b = 0
    elif when <= 18000:
        r = 85
        g = 13
        b = 1
    elif when <= 21600:
        r = 100
        g = 18
        b = 2
    elif when <= 25200:
        r = 200
        g = 36
        b = 4
    elif when <= 39600:
        r = 255
        g = 125
        b = 25
    elif when <= 54000:
        r = 255
        g = 200
        b = 75
    elif when <= 61200:
        r = 255
        g = 125
        b = 25
    elif when <= 64800:
        r = 200
        g = 36
        b = 4
    elif when <= 68400:
        r = 100
        g = 18
        b = 2
    elif when <= 72000:
        r = 85
        g = 13
        b = 1
    elif when <= 86400:
        r = 75
        g = 10
        b = 0
    else:
        when = 0
    effects.rgbInstance(r, g, b)
    diff2 = time.time()
    end = time.time()
effects.kill()
