#!/usr/bin/python3
#!/usr/bin/env python3

import numpy as np
from scipy import signal
import simpleaudio as sa
import RPi.GPIO as GPIO
import time

def Sham_SlowOsci():
    
    pinNum = (22, 14)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pinNum,GPIO.OUT)
    GPIO.output(pinNum,(GPIO.HIGH,GPIO.HIGH))
    time.sleep(0.001)
    GPIO.output(pinNum,(GPIO.HIGH,GPIO.LOW))
    
    sample_rate = 44100

    audio = np.load('slowosc_sham.npy')

    # normalize to 16-bit range
    audio *= 32767 / np.max(np.abs(audio))
    # convert to 16-bit data
    audio = audio.astype(np.int16)

    # start playback
    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)

    # wait for playback to finish before exiting
    #play_obj.wait_done()

    GPIO.cleanup()