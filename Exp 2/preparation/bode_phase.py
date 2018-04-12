# bode phase plot of three fucking low pass filters

import numpy as np
import matplotlib.pyplot as plt

freq = np.linspace(0, 1e6, 5e5)

f1 = 100
f2 = 1000
f3 = 10000

phase = -180/np.pi * (np.arctan(freq / f1) + np.arctan(freq / f3) + np.arctan(freq / f3))

plt.plot(freq, phase, color = 'r')
plt.xscale('log')
plt.show()
