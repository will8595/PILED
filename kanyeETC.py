# !/usr/bin/env python
# The song is Kanye by The Chainsmokers (ETC! ETC! remix)
# Start this program at the exact time that the song starts.
# Working on making the program start the audio when the lights start...

import effects

import time


def start():
    start = time.time()
    effects.whiteSoftFade(0.016, 1)
    # 4.3 Secs
    # fstart = time.time()
    for i in range(6):
        effects.red(.25, 64)
        effects.red(.25, 32)
    # fstart = time.time()
    for i in range(4):
        effects.blueSoftFade(.001, 1)
    # fstart = time.time()
    for i in range(5):
        effects.red(.25, 64)
        effects.red(.25, 32)
    effects.red(.25, 64)
    # 11.90 secs
    # fstart = time.time()
    effects.blueSoftFade(.221, 32)
    # 13.74 secs Lyrics begin, begin longterm fade
    # fstart = time.time()
    effects.rgbCrossFade(0.008, 4, 2)
    # 27.39 secs
    # fstart = time.time()
    effects.rgbSoftBuild(0.007, 4, 2)
    # 39.37 secs
    # fstart = time.time()
    effects.kill(1.76)
    # 40.09 secs
    # fstart = time.time()
    effects.whiteSoftFade(0.053, 1)
    # 54.8 secs
    effects.rgbStrobe(0.44444444, 9)  # .5, 8
    # 66.9 secs #f time 12.1
    effects.kill(1.657)
    # 68.6 secs
    effects.strobeWhite(6.85)
    # 75.630 secs
    effects.rgbCrossFade(0.0036, 8, 4)
    # 82.5 secs
    effects.rgbSoftBuild(0.003475, 15, 4)
    # 94.34 secs
    effects.blueSoftFade(0.016, 4)
    # 95.35 secs
    effects.rgbCrossFade(0.0075, 8, 2)
    # 121.56 secs
    effects.kill(1.894)
    # 123.454
    effects.whiteSoftFade(0.016, 1)
    # 127.768
    effects.rgbStrobe(0.39, 8)
    # ~137.166
    effects.rgbJumpBuild(0.45, 0.25, 36)
    # ~148.598
    effects.white(0.59)
    effects.kill(1.703)  # 3 used to be a 2
    # vvv copied from above vvv
    effects.strobeWhite(6.85)
    effects.rgbCrossFade(0.0036, 8, 4)
    effects.rgbSoftBuild(0.003475, 15, 4)
    effects.blueSoftFade(0.016, 4)
    # ~178.0
    # End Sequence:
    effects.rgbCrossFade(0.0075, 4, 2)
    effects.redSoftFade(0.022, 2)
    total = time.time() - start
    print(total)
    effects.kill()


def main():
    start()

main()
