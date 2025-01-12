import numpy as np
import matplotlib.pyplot as plt

#Carrier wave c(t)=A_c*cos(2*pi*f_c*t)
#Modulating wave m(t)=A_m*cos(2*pi*f_m*t)
#Modulated wave s(t)=A_c[1+mu*cos(2*pi*f_m*t)]cos(2*pi*f_c*t)

A_c = float(input('Enter carrier amplitude: '))
f_c = float(input('Enter carrier frquency: '))
A_m = float(input('Enter modulation amplitude: '))
f_m = float(input('Enter modulation frquency: '))
k = float(input('Enter modulation index: '))

t = np.linspace(0, 1, 500)

carrier = A_c*np.cos(2*np.pi*f_c*t)
modulator = A_m*np.cos(2*np.pi*f_m*t)

product_cl = carrier + modulator
fftfreq_cl = np.fft.rfftfreq(product_cl.shape[0], 1.0/len(t))
fft_cl = np.abs(np.fft.rfft(product_cl))

product_SCDSB = carrier * modulator
fftfreq_SCDSB = np.fft.rfftfreq(product_SCDSB.shape[0], 1.0/len(t))
fft_SCDSB = np.abs(np.fft.rfft(product_SCDSB))

product_WCDSB = carrier * (1 + k * modulator)
fftfreq_WCDSB = np.fft.rfftfreq(product_WCDSB.shape[0], 1.0/len(t))
fft_WCDSB = np.abs(np.fft.rfft(product_WCDSB))

plt.subplot(8,1,2)
plt.plot(modulator,'g')
plt.xlabel('Modulation Wave')

plt.subplot(8,1,1)
plt.plot(carrier, 'r')
plt.xlabel('Carrier wave')

plt.subplot(8,1,3)
plt.title('Classical Amplitude Modulation')
plt.plot(product_cl, color="purple")
plt.xlabel('AM signal')

plt.subplot(8,1,4)
plt.plot(fftfreq_cl, fft_cl, color="blue")
plt.xlabel('FFT')

plt.subplot(8,1,5)
plt.title('Suppresed Carrier Double Side Band Amplitude Modulation')
plt.plot(product_SCDSB, color="purple")
plt.xlabel('AM signal')

plt.subplot(8,1,6)
plt.plot(fftfreq_SCDSB, fft_SCDSB, color="blue")
plt.xlabel('FFT')

plt.subplot(8,1,7)
plt.title('With Carrier Double Side Band Amplitude Modulation')
plt.plot(product_WCDSB, color="purple")
plt.xlabel('AM signal')

plt.subplot(8,1,8)
plt.plot(fftfreq_WCDSB, fft_WCDSB, color="blue")
plt.xlabel('FFT')

plt.subplots_adjust(hspace=3)
plt.rc('font', size=10)
fig = plt.gcf()
fig.set_size_inches(16, 9)

fig.savefig('Amplitude Modulation.png', dpi=100)