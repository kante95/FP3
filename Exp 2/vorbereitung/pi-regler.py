# PI - Regler : einfach noch an Integrator addieren?

import matplotlib.pyplot as plt
import numpy as np

# Strecke
freq = np.linspace(1, 1e6, 5e5)

f1 = 100
f2 = 1000
f3 = 10000

# P-Regler
A_p = 19
A_p = np.ones(500000) * A_p

# Integrator
f_i = 71.5
k = -20
A_i = k * np.log10(freq) - k * np.log10(f_i)
A_i[A_i < 0] = 0

phase_i = -90 + 180 / np.pi * np.arctan(freq / f_i)

# amlitude Regler
A_r = A_p + A_i

# amplitude
amp = -10 * np.log10((1 + (freq / f1)**2) * (1 + (freq / f2)**2) * (1 + (freq / f3)**2))

# total
A_t = amp + A_r

# phase
phase = -180/np.pi * (np.arctan(freq / f1) + np.arctan(freq / f3) + np.arctan(freq / f3))
phase = phase + phase_i

# Plot all the things
plt.plot(freq, amp, color = 'r', label = r'$A_S$')
plt.plot(freq, A_r, 'k--', label = r'$A_P$')
plt.plot(freq, A_t, 'k-', label = r'$A_S \cdot A_P$')
plt.xlabel(r'$f$ / Hz')
plt.ylabel(r'$A$ / dB')
plt.xscale('log')
plt.legend()
plt.show()

plt.plot(freq, phase, color = 'r')
plt.xlabel(r'$f$ / Hz')
plt.ylabel(r'$\varphi$ / Degree')
plt.xscale('log')
plt.show()
