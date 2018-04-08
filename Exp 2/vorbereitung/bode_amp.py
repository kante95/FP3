# Bode Amplitude plot of three fucking serial low pass filters

import matplotlib.pyplot as plt
import numpy as np


freq = np.linspace(0, 1e6, 5e5)

f1 = 100
f2 = 1000
f3 = 10000

amp = -10 * np.log10((1 + (freq / f1)**2) * (1 + (freq / f2)**2) * (1 + (freq / f3)**2))# + (freq / f2)**4) + (freq / f3)**6)

plt.plot(freq, amp, color = 'r')
plt.xscale('log')
plt.show()
