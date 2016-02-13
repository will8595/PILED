#!/usr/bin/env python
#(c) 2015 William McLaughlin
#Version 1.0.2
# ========== Change Log ==========
# * Fixed code error in rgbStrobe()

import pigpio
import time

RED = 17
GREEN = 22
BLUE = 24
pi = pigpio.pi()

def kill(duration = 0):
    pi.set_PWM_dutycycle(RED, 0)
    pi.set_PWM_dutycycle(GREEN, 0)
    pi.set_PWM_dutycycle(BLUE, 0)
    time.sleep(duration)

def strobeWhite(duration = 3, speed = 0.1):
    index = 0
    cycles = duration / (2 * speed)
    while index < cycles:
        pi.set_PWM_dutycycle(RED, 255)
        pi.set_PWM_dutycycle(GREEN, 255)
        pi.set_PWM_dutycycle(BLUE, 255)
        #STROBE PAUSE
        time.sleep(speed)
        pi.set_PWM_dutycycle(RED, 0)
        pi.set_PWM_dutycycle(GREEN, 0)
        pi.set_PWM_dutycycle(BLUE, 0)
        #STROBE PAUSE
        time.sleep(speed)
        index += 1

def strobeRed(duration = 3, speed = 0.1):
    index = 0
    cycles = duration / (2 * speed)
    while index < cycles:
        pi.set_PWM_dutycycle(RED, 255)
        pi.set_PWM_dutycycle(GREEN, 0)
        pi.set_PWM_dutycycle(BLUE, 0)
        #STROBE PAUSE
        time.sleep(speed)
        pi.set_PWM_dutycycle(RED, 0)
        pi.set_PWM_dutycycle(GREEN, 0)
        pi.set_PWM_dutycycle(BLUE, 0)
        #STROBE PAUSE
        time.sleep(speed)
        index += 1

def strobeGreen(duration = 3, speed = 0.1):
    index = 0
    cycles = duration / (2 * speed)
    while index < cycles:
        pi.set_PWM_dutycycle(RED, 0)
        pi.set_PWM_dutycycle(GREEN, 255)
        pi.set_PWM_dutycycle(BLUE, 0)
        #STROBE PAUSE
        time.sleep(speed)
        pi.set_PWM_dutycycle(RED, 0)
        pi.set_PWM_dutycycle(GREEN, 0)
        pi.set_PWM_dutycycle(BLUE, 0)
        #STROBE PAUSE
        time.sleep(speed)
        index += 1

def strobeBlue(duration = 3, speed = 0.1):
    index = 0
    cycles = duration / (2 * speed)
    while index < cycles:
        pi.set_PWM_dutycycle(RED, 0)
        pi.set_PWM_dutycycle(GREEN, 0)
        pi.set_PWM_dutycycle(BLUE, 255)
        #STROBE PAUSE
        time.sleep(speed)
        pi.set_PWM_dutycycle(RED, 0)
        pi.set_PWM_dutycycle(GREEN, 0)
        pi.set_PWM_dutycycle(BLUE, 0)
        #STROBE PAUSE
        time.sleep(speed)
        index += 1

def strobeCustom(rbright, gbright, bbright, duration = 3, speed = 0.1):
    index = 0
    cycles = duration / (2 * speed)
    while index < cycles:
        pi.set_PWM_dutycycle(RED, rbright)
        pi.set_PWM_dutycycle(GREEN, gbright)
        pi.set_PWM_dutycycle(BLUE, bbright)
        #STROBE PAUSE
        time.sleep(speed)
        pi.set_PWM_dutycycle(RED, 0)
        pi.set_PWM_dutycycle(GREEN, 0)
        pi.set_PWM_dutycycle(BLUE, 0)
        #STROBE PAUSE
        time.sleep(speed)
        index += 1

def rgbStrobe(speed, cycles):
    ctr = 0
    while ctr < cycles:
        pi.set_PWM_dutycycle(RED, 255)
        pi.set_PWM_dutycycle(GREEN, 0)
        pi.set_PWM_dutycycle(BLUE, 0)
        time.sleep(speed)
        pi.set_PWM_dutycycle(RED, 0)
        pi.set_PWM_dutycycle(GREEN, 255)
        pi.set_PWM_dutycycle(BLUE, 0)
        time.sleep(speed)
        pi.set_PWM_dutycycle(RED, 0)
        pi.set_PWM_dutycycle(GREEN, 0)
        pi.set_PWM_dutycycle(BLUE, 255)
        time.sleep(speed)
        ctr += 1

def rgbJumpBuild(startSpeed, stopSpeed, cycles):
    #This function is best followed by rgbStrobe([duration], stopSpeed)
    #example:
    #def strobeHold(startSpeed, endSpeed, cycles):
    #    rgbJumpBuild(startSpeed, endSpeed, cycles)
    #    rgbStrobe(endSpeed, cycles)
    #strobeHold(1, 0.1, 10)
    ctr = 0
    speed = startSpeed - stopSpeed
    speedStep = speed / cycles
    while ctr < cycles:
        pi.set_PWM_dutycycle(RED, 255)
        pi.set_PWM_dutycycle(GREEN, 0)
        pi.set_PWM_dutycycle(BLUE, 0)
        time.sleep(speed)
        pi.set_PWM_dutycycle(RED, 0)
        pi.set_PWM_dutycycle(GREEN, 255)
        pi.set_PWM_dutycycle(BLUE, 0)
        time.sleep(speed)
        pi.set_PWM_dutycycle(RED, 0)
        pi.set_PWM_dutycycle(GREEN, 0)
        pi.set_PWM_dutycycle(BLUE, 255)
        time.sleep(speed)
        ctr += 1
        speed -= speedStep

def white(duration, brightness = 255):
    pi.set_PWM_dutycycle(RED, brightness)
    pi.set_PWM_dutycycle(GREEN, brightness)
    pi.set_PWM_dutycycle(BLUE, brightness)
    time.sleep(duration)

def red(duration, brightness = 255):
    pi.set_PWM_dutycycle(RED, brightness)
    pi.set_PWM_dutycycle(GREEN, 0)
    pi.set_PWM_dutycycle(BLUE, 0)
    time.sleep(duration)

def orange(duration, brightness = 255):
    gbright = int(brightness / 2.5)
    pi.set_PWM_dutycycle(RED, brightness)
    pi.set_PWM_dutycycle(GREEN, gbright)
    pi.set_PWM_dutycycle(BLUE, 0)
    time.sleep(duration)

def yellow(duration, brightness = 255):
    pi.set_PWM_dutycycle(RED, brightness)
    pi.set_PWM_dutycycle(GREEN, brightness)
    pi.set_PWM_dutycycle(BLUE, 0)
    time.sleep(duration)

def green(duration, brightness = 255):
    pi.set_PWM_dutycycle(RED, 0)
    pi.set_PWM_dutycycle(GREEN, brightness)
    pi.set_PWM_dutycycle(BLUE, 0)
    time.sleep(duration)

def blue(duration, brightness = 255):
    pi.set_PWM_dutycycle(RED, 0)
    pi.set_PWM_dutycycle(GREEN, 0)
    pi.set_PWM_dutycycle(BLUE, brightness)
    time.sleep(duration)

def purple(duration, brightness = 255):
    rbright = int(brightness / 1.25)
    pi.set_PWM_dutycycle(RED, rbright)
    pi.set_PWM_dutycycle(GREEN, 0)
    pi.set_PWM_dutycycle(BLUE, brightness)
    time.sleep(duration)

def rgbSet(redBrightness, greenBrightness, blueBrightness, duration = 5):
    pi.set_PWM_dutycycle(RED, redBrightness)
    pi.set_PWM_dutycycle(GREEN, greenBrightness)
    pi.set_PWM_dutycycle(BLUE, blueBrightness)
    time.sleep(duration)

def rgbInstance(red, green, blue):
    pi.set_PWM_dutycycle(RED, red)
    pi.set_PWM_dutycycle(GREEN, green)
    pi.set_PWM_dutycycle(BLUE, blue)

def whiteSoftBuild(speed, step):
    bright = 255
    index = 0
    while index <= 255:
        pi.set_PWM_dutycycle(RED, bright)
        pi.set_PWM_dutycycle(GREEN, bright)
        pi.set_PWM_dutycycle(BLUE, bright)
        index += step
        bright += step
        time.sleep(speed)

def redSoftBuild(speed, step):
    rbright = 0
    index = 0
    while index <= 255:
        pi.set_PWM_dutycycle(RED, rbright)
        pi.set_PWM_dutycycle(GREEN, 0)
        pi.set_PWM_dutycycle(BLUE, 0)
        index += step
        rbright += step
        time.sleep(speed)

def greenSoftBuild(speed, step):
    gbright = 0
    index = 0
    while index <= 255:
        pi.set_PWM_dutycycle(RED, 0)
        pi.set_PWM_dutycycle(GREEN, gbright)
        pi.set_PWM_dutycycle(BLUE, 0)
        index += step
        gbright += step
        time.sleep(speed)

def blueSoftBuild(speed, step):
    bbright = 0
    index = 0
    while index <= 255:
        pi.set_PWM_dutycycle(RED, 0)
        pi.set_PWM_dutycycle(GREEN, 0)
        pi.set_PWM_dutycycle(BLUE, bbright)
        index += step
        bbright += step
        time.sleep(speed)

def whiteSoftFade(speed, step):
    bright = 255
    index = 0
    while index <= 255:
        pi.set_PWM_dutycycle(RED, bright)
        pi.set_PWM_dutycycle(GREEN, bright)
        pi.set_PWM_dutycycle(BLUE, bright)
        index += step
        bright -= step
        time.sleep(speed)

def redSoftFade(speed, step):
    rbright = 255
    index = 0
    while index <= 255:
        pi.set_PWM_dutycycle(RED, rbright)
        pi.set_PWM_dutycycle(GREEN, 0)
        pi.set_PWM_dutycycle(BLUE, 0)
        index += step
        rbright -= step
        time.sleep(speed)

def greenSoftFade(speed, step):
    gbright = 255
    index = 0
    while index <= 255:
        pi.set_PWM_dutycycle(RED, 0)
        pi.set_PWM_dutycycle(GREEN, gbright)
        pi.set_PWM_dutycycle(BLUE, 0)
        index += step
        gbright -= step
        time.sleep(speed)

def blueSoftFade(speed, step):
    bbright = 255
    index = 0
    while index <= 255:
        pi.set_PWM_dutycycle(RED, 0)
        pi.set_PWM_dutycycle(GREEN, 0)
        pi.set_PWM_dutycycle(BLUE, bbright)
        index += step
        bbright -= step
        time.sleep(speed)

def rgbCrossFade(speed, cycles, step):
    rbright = 255
    gbright = 0
    bbright = 0
    run = True
    stop = False
    ctr = 0
    while run and ctr < cycles:
        if rbright > 0 and not stop:
            pi.set_PWM_dutycycle(RED, rbright)
            pi.set_PWM_dutycycle(GREEN, gbright)
            pi.set_PWM_dutycycle(BLUE, bbright)
            if rbright <= step:
                rbright = 0
                gbright = 255
            else:
                rbright -= step
                gbright += step
            time.sleep(speed)
        elif gbright > 0:
            pi.set_PWM_dutycycle(RED, rbright)
            pi.set_PWM_dutycycle(GREEN, gbright)
            pi.set_PWM_dutycycle(BLUE, bbright)
            if gbright <= step:
                gbright = 0
                bbright = 255
            else:
                gbright -= step
                bbright += step
            time.sleep(speed)
        elif bbright > 0:
            #Pushes it to else once blue is all the way back down
            #and prevents it from being a continuous loop
            stop = True
            pi.set_PWM_dutycycle(RED, rbright)
            pi.set_PWM_dutycycle(GREEN, gbright)
            pi.set_PWM_dutycycle(BLUE, bbright)
            if bbright <= step:
                bbright = 0
                rbright = 255
            else:
                bbright -= step
                rbright += step
            time.sleep(speed)
        else:
            if ctr < cycles:
                ctr += 1
                #Stop is set to false so the loop is able to restart again
                stop = False
            else:
                run = False

def rgbSoftFade(speed, cycles, step):
    rbright = 255
    gbright = 0
    bbright = 0
    run = True
    stop = False
    ctr = 0
    while run and ctr < cycles:
        if rbright > 0 and not stop:
            pi.set_PWM_dutycycle(RED, rbright)
            pi.set_PWM_dutycycle(GREEN, gbright)
            pi.set_PWM_dutycycle(BLUE, bbright)
            if rbright <= step:
                rbright = 0
                gbright = 255
            else:
                rbright -= step
            time.sleep(speed)
        elif gbright > 0:
            pi.set_PWM_dutycycle(RED, rbright)
            pi.set_PWM_dutycycle(GREEN, gbright)
            pi.set_PWM_dutycycle(BLUE, bbright)
            if gbright <= step:
                gbright = 0
                bbright = 255
            else:
                gbright -= step
            time.sleep(speed)
        elif bbright > 0:
            #Pushes it to else once blue is all the way back down
            #and prevents it from being a continuous loop
            stop = True
            pi.set_PWM_dutycycle(RED, rbright)
            pi.set_PWM_dutycycle(GREEN, gbright)
            pi.set_PWM_dutycycle(BLUE, bbright)
            if bbright <= step:
                bbright = 0
                rbright = 255
            else:
                bbright -= step
            time.sleep(speed)
        else:
            if ctr < cycles:
                ctr += 1
                #Stop is set to false so the loop is able to restart again
                stop = False
            else:
                run = False

def rgbSoftBuild(speed, cycles, step):
    rbright = 0
    gbright = 0
    bbright = 0
    run = True
    stop = False
    ctr = 0
    checkRed = True
    checkGreen = True
    checkBlue = True
    while run and ctr < cycles:
        if checkRed:
            pi.set_PWM_dutycycle(RED, rbright)
            pi.set_PWM_dutycycle(GREEN, gbright)
            pi.set_PWM_dutycycle(BLUE, bbright)
            if rbright >= (255 - step):
                rbright = 255
                gbright = 0
                checkRed = False
            else:
                rbright += step
            time.sleep(speed)
        elif checkGreen:
            rbright = 0
            pi.set_PWM_dutycycle(RED, rbright)
            pi.set_PWM_dutycycle(GREEN, gbright)
            pi.set_PWM_dutycycle(BLUE, bbright)
            if gbright >= (255 - step):
                gbright = 255
                bbright = 0
                checkGreen = False
            else:
                gbright += step
            time.sleep(speed)
        elif checkBlue:
            gbright = 0
            pi.set_PWM_dutycycle(RED, rbright)
            pi.set_PWM_dutycycle(GREEN, gbright)
            pi.set_PWM_dutycycle(BLUE, bbright)
            if bbright >= (255 - step):
                bbright = 255
                rbright = 0
                checkBlue = False
            else:
                bbright += step
            time.sleep(speed)
        else:
            bbright = 0
            if ctr < cycles:
                ctr += 1
                #Stop is set to false so the loop is able to restart again
                checkRed = True
                checkGreen = True
                checkBlue = True
            else:
                run = False
