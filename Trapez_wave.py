# Cutting up a Sawtooth signal for rtDCS
from scipy import signal
#import matplotlib.pyplot as plt
import numpy as np
import simpleaudio as sa

# numb =  3 # Number of seconds    
# # Time --> Sampling: 250 Hz
# time = np.linspace(0, 1*numb, 250*numb, endpoint=True)

###
sample_rate = 44100
T = 6
time = np.linspace(0, T, T * sample_rate, False)
###

# Sawtooth 
tria = 1 + signal.sawtooth(2*np.pi*0.75*time, 1/2)

# Square signal --> 33% Duty Cycle Pulse waveform
squa = 1 + (1/3)*signal.square(2*np.pi*0.75*time + (np.pi+np.pi/3), 1/3)

# Plot singles
#plt.figure(1)
#plt.plot(time,tria)
#plt.plot(time,squa)

# Plot coupled
coupled = np.ones(len(time))
#plt.plot(time,coupled)
for i in range(time.shape[0]):
    if tria[i] > 2/3 and tria[i] < 4/3:
        coupled[i] = tria[i]
    elif tria[i] < 2/3 or tria[i] < 4/3:
        coupled[i] = squa[i]
    else:
        coupled[i] = squa[i]
coupled = coupled - 1
coupled = (1/max(coupled))*coupled +1
#plt.figure(2)
#plt.plot(time,coupled)

# # concatenate notes
audio = np.hstack((coupled))#, Csh_note, E_note))
# # normalize to 16-bit range
audio *= 32767 / np.max(np.abs(audio))
# # convert to 16-bit data
audio = audio.astype(np.int16)

# # start playback
play_obj = sa.play_buffer(audio, 1, 2, sample_rate)

# # wait for playback to finish before exiting
play_obj.wait_done()

