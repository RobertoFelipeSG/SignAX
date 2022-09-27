#!/usr/bin/python3
#!/usr/bin/env python3

import os
os.system('sudo killall pigpiod')
os.system('sudo pigpiod')

import time
import pigpio
# wave_PWM.py
# 2016-03-19
# Public Domain --> Based on the code from PIGPIOD Website

#def SlowOsc_rtDCS():
    
FREQ=1.5 # The PWM cycles per second.
PWM1=18
GPIO=PWM1

_micros=int(1000000/FREQ)
old_wid = None

def set_dc(dc):

   global old_wid

   if dc < 0:
      dc = 0
   elif dc > _micros:
      dc = _micros

   d = dc
   g = GPIO
   if d == 0:
      pi.wave_add_generic([pigpio.pulse(0, 1<<g, _micros)])
   elif d == _micros:
      pi.wave_add_generic([pigpio.pulse(1<<g, 0, _micros)])
   else:
      pi.wave_add_generic(
            [pigpio.pulse(1<<g, 0, d), pigpio.pulse(0, 1<<g, _micros-d)])

   new_wid = pi.wave_create()

   if old_wid is not None:

      pi.wave_send_using_mode(new_wid, pigpio.WAVE_MODE_REPEAT_SYNC)

      # Spin until the new wave has started.
      def s():
          if pi.wave_tx_at() != new_wid:
              pass
          #self.after(1,s)
      selfie.after(1,s) 

      # It is then safe to delete the old wave.
      pi.wave_delete(old_wid)

   else:
      pi.wave_send_repeat(new_wid)

   old_wid = new_wid



pi = pigpio.pi()
if not pi.connected:
   exit(0)

# Need to explicity set wave GPIO to output mode.

pi.set_mode(GPIO, pigpio.OUTPUT)

for i in range(180): #Quantity of cycles 180*1.333=240s

   set_dc(int(_micros/2))
   #stime.sleep(0.5)

pi.wave_tx_stop()

if old_wid is not None:
   pi.wave_delete(old_wid)

pi.stop()



