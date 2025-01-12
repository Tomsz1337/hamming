import math
import numpy as np
import matplotlib.pyplot as plt

# Set the parameters of the sine wave

amplitude = 1 # Amplitude of the wave

frequency = 1 # Frequency of the wave in Hertz

phase = 0 # Phase shift of the wave in radians

sampling_rate = 100 # Number of samples per second

duration = 1 # Duration of the wave in seconds

# Create a numpy array of time values from 0 to duration

def input_param(sine_amp, sine_freq, sine_phase, sqr_amp, sqr_freq, sqr_phase, s_r, duration):

    time = np.linspace(0, duration, int(duration * s_r), endpoint=False)
    sine_wave = sine_amp * np.sin(2 * np.pi * sine_freq * time + sine_phase)
    sqr1 = sqr_amp * np.sin(2 * np.pi * sqr_freq * time + sqr_phase)
    sqr2 = (sqr_amp/3) * np.sin(2 * np.pi * sqr_freq *3 * time + sqr_phase)
    sqr3 = (sqr_amp/5) * np.sin(2 * np.pi * sqr_freq *5 * time + sqr_phase)
    #sqr4 = (sqr_amp/7) * np.sin(2 * np.pi * sqr_freq *7 * time + sqr_phase)
    sqr_wave = sqr1 + sqr2 + sqr3
    x = sine_wave * sqr_wave
    dot = sine_wave @ sqr_wave
    print(dot)
    return time, sine_wave, sqr_wave, x

# Calculate the sine wave values for each time value



# Plot the sine wave
param = input_param(1,8,0,1,2,0,100,2)

fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.suptitle('Vertically stacked subplots')
ax1.plot(param[0], param[1])
ax2.plot(param[0], param[2])
ax3.plot(param[0], param[3])


#plt.plot(sine_param[0], sine_param[1])

#plt.xlabel('Time (seconds)')

#plt.ylabel('Amplitude')

#plt.title('Sine Wave Generator')

plt.show()