# p Regler - addiere const Wert zum Diagramm der Strecke

import matplotlib.pyplot as plt
import numpy as np

# Strecke
freq = np.linspace(0, 1e6, 5e5)

f1 = 100
f2 = 1000
f3 = 10000

# P-Regler
A_p = 19
A_p = np.ones(500000) * A_p

# amplitude
amp = -10 * np.log10((1 + (freq / f1)**2) * (1 + (freq / f2)**2) * (1 + (freq / f3)**2))# + (freq / f2)**4) + (freq / f3)**6)

# phase
phase = -180/np.pi * (np.arctan(freq / f1) + np.arctan(freq / f3) + np.arctan(freq / f3))

plt.plot(freq, amp, color = 'r', label = r'$A_S$')
plt.plot(freq, A_p, 'k--', label = r'$A_P$')
plt.plot(freq, amp + A_p, 'k-', label = r'$A_S \cdot A_P$')
plt.xscale('log')
plt.show()

plt.plot(freq, phase, color = 'r')
plt.xscale('log')
plt.show()
