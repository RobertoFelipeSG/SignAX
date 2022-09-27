import RPi.GPIO as GPIO
import time

pinNum = 14
pinNum1 = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinNum,GPIO.OUT)
#GPIO.setup(pinNum1,GPIO.OUT)
GPIO.output(pinNum,GPIO.HIGH)
#GPIO.output(pinNum1,GPIO.LOW)
time.sleep(0.001)
GPIO.output(pinNum,GPIO.LOW)
#GPIO.output(pinNum1,GPIO.HIGH)

#GPIO.cleanup()



