import numpy as np
import matplotlib.pyplot as plt

# Signal parameters
f1 = 50  # Frequency of first sine wave
f2 = 120  # Frequency of second sine wave
fs = 1000  # Sampling frequency
T = 1  # Duration in seconds

# Time vector
t = np.linspace(0, T, fs*T, endpoint=False)

# Signal definition
s = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

# Compute FFT
S = np.fft.fft(s)
# Compute frequencies
frequencies = np.fft.fftfreq(len(S), 1/fs)

# Only take the positive frequencies
positive_frequencies = frequencies[:len(frequencies)//2]
positive_S = np.abs(S[:len(S)//2])  # Magnitude of FFT

# Plot the signal
plt.figure(figsize=(12, 6))

# Plot time domain signal
plt.subplot(2, 1, 1)
plt.plot(t, s)
plt.title('Time Domain Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Plot frequency domain signal
plt.subplot(2, 1, 2)
plt.plot(positive_frequencies, positive_S)
plt.title('Frequency Domain Signal')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.grid()
plt.tight_layout()
plt.show()
