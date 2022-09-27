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

#from SlowOsc_rtDCS import *
from Spindles_tACS import *

win = tk.Tk()

myFont = tk.font.Font(family = 'Helvetica', size = 30, weight = 'bold')

def Spindles():
    print('Stimulating with Spindles')
    Spindles_tACS()

def SlowOsci():
    print('Stimulating with Slow Oscillations')
    os.system('python SlowOsc_rtDCS.py')
    
def Abort():
    print("Exit Button pressed")
    #win.quit()
    os.system('sudo killall pigpiod')
    python = sys.executable
    os.execl(python, python, * sys.argv)

win.title("Sleep Stimulation")
win.geometry('750x450')

buttons = ['Spindles', 'Slow Osci', 'Abort']

but1 = tk.Button(win, text=buttons[0], width=10, height=5, bg="#ffb6c1", activebackground="#ffffff", font =myFont,
                        activeforeground="#000000", highlightthickness=4, command=Spindles)#_tACS)
but1.grid(row=0, column=0)
but2 = tk.Button(win, text=buttons[1], width=10, height=5, bg="#ffb6c1", activebackground="#ffffff", font =myFont,
                        activeforeground="#000000", highlightthickness=4, command=SlowOsci)#SlowOsci_rtDCS)
but2.grid(row=0, column=2)
but3 = tk.Button(win, text=buttons[2], width=10, height=3, bg="#000000", fg="#ffffff", highlightthickness=4,
                        font =myFont, activebackground="#ffffff", activeforeground="#000000", relief="raised",
                        padx=4, pady=4, bd=4, command=Abort)
but3.grid(row=1, column=1)

win.mainloop()