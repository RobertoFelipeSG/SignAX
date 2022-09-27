import RPi.GPIO as GPIO
import time
    
pinNum = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinNum,GPIO.OUT)
for i in range(50):
    GPIO.output(pinNum,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pinNum,GPIO.LOW)
    time.sleep(1)
            
