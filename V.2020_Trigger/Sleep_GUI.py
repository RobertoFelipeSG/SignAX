#!/usr/bin/python3
#!/usr/bin/env python3

import sys
import os

import tkinter as tk
import time
from tkinter import *
from tkinter import font
from tkinter import Button
#from PIL import Image, ImageTk
from time import sleep
import RPi.GPIO as GPIO

from Spindles_tACS import *
from SlowOsc_rtDCS import *
from Sham_Spindles import *
from Sham_SlowOsci import *

win = tk.Tk()

myFont = tk.font.Font(family = 'Helvetica', size = 30, weight = 'bold')

def stACS():
    print('Stimulating with Spindles')
    Spindles_tACS()

def rtDCS():
    print('Stimulating with Slow Oscillations')
    SlowOsc_rtDCS()
        
def Sham_stACS():
    print('Stimulating with Sham Spindles')
    Sham_Spindles()

def Sham_rtDCS():
    print('Stimulating with Sham Slow Oscillations')
    Sham_SlowOsci()
    
def Abort():
    print("Exit Button pressed")
    marker_on = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(marker_on,GPIO.OUT)
    GPIO.output(marker_on,GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(marker_on,GPIO.LOW)
    #win.quit()
    os.system('sudo killall pigpiod')
    python = sys.executable
    os.execl(python, python, * sys.argv)

win.title("Sleep Stimulation")
win.geometry('750x450')

buttons = ['stACS', 'rtDCS', 'Sham stACS', 'Sham rtDCS', 'Abort']

but1 = tk.Button(win, text=buttons[0], width=10, height=3, bg="#ffb6c1", activebackground="#ffffff", font =myFont,
                        activeforeground="#000000", highlightthickness=4, command=stACS)#_tACS)
but1.grid(row=0, column=0)
but2 = tk.Button(win, text=buttons[1], width=10, height=3, bg="#ffb6c1", activebackground="#ffffff", font =myFont,
                        activeforeground="#000000", highlightthickness=4, command=rtDCS)#SlowOsci_rtDCS)
but2.grid(row=0, column=2)
but3 = tk.Button(win, text=buttons[2], width=10, height=3, bg="#ffb6c1", activebackground="#ffffff", font =myFont,
                        activeforeground="#000000", highlightthickness=4, command=Sham_stACS)#Sham_tACS)
but3.grid(row=2, column=0)
but4 = tk.Button(win, text=buttons[3], width=10, height=3, bg="#ffb6c1", activebackground="#ffffff", font =myFont,
                        activeforeground="#000000", highlightthickness=4, command=Sham_rtDCS)#Sham_SlowOsci)
but4.grid(row=2, column=2)
but5 = tk.Button(win, text=buttons[4], width=10, height=2, bg="#000000", fg="#ffffff", highlightthickness=4,
                        font =myFont, activebackground="#ffffff", activeforeground="#000000", relief="raised",
                        padx=4, pady=4, bd=4, command=Abort)
but5.grid(row=1, column=1)

win.mainloop()