import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sp

def lorentz(x, a, gamma, x0, b):
    return a * (gamma**2)/(gamma**2 + (x - x0)**2) + b

# Paths
AngioI_HRes = 'AngioI_HRes/AngioI_HRes_000001.d/xy1.dx'
AngioI_cal_HR_250 = "AngioI_cal_HR_250/AngioI_cal_HR_250x_000001.d/xy1.dx"


mass, intensity = np.loadtxt(AngioI_cal_HR_250, delimiter = ',', unpack = True)

mass = mass[(mass > 432.92) & (mass < 432.93)]
intensity = intensity[(mass > 432.92) & (mass < 432.93)]

#params, pcov = sp.curve_fit(lorentz, mass, intensity, p0 = ())

plt.plot(mass, intensity, color = 'k')
plt.xlabel(r'$m/z$ in $\frac{\mathrm{u}}{e}$')
plt.ylabel(r'Intensity')
plt.tight_layout()
#plt.savefig('hires_spectrum.pdf', format = 'pdf')
plt.show()
