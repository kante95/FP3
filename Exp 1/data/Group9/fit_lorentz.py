import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sp

def lorentz(x, a, gamma, x0, b):
    return a * (gamma**2)/(gamma**2 + (x - x0)**2) + b

# Paths
AngioI_HRes = 'AngioI_HRes/AngioI_HRes_000001.d/xy1.dx'
AngioI_cal_HR_250 = "AngioI_cal_HR_250/AngioI_cal_HR_250x_000001.d/xy1.dx"


mass1, intensity1 = np.loadtxt(AngioI_cal_HR_250, delimiter = ',', unpack = True)

mass = mass1[(mass1 > 432.92) & (mass1 < 432.93)]
intensity = intensity1[(mass1 > 432.92) & (mass1 < 432.93)]

params, pcov = sp.curve_fit(lorentz, mass, intensity, p0 = (2e8, 0.0001, 432.925, 0))
print("Resolution: " + str(params[2]/(2 * params[1])))
err = np.sqrt(np.diag(pcov))
print(params, err)
plt.plot(mass, intensity)
plt.plot(mass, lorentz(mass, *params))
plt.xlabel(r'$m/z$ in $\frac{\mathrm{u}}{e}$')
plt.ylabel(r'Intensity')
plt.tight_layout()
plt.savefig('fit_hires.pdf', format = 'pdf')
plt.show()

reso = params[2] / (2 * params[1])
dreso = np.sqrt((err[2] / (2 * params[1]))**2 + (params[2] * err[1] / (2 * params[1]**2))**2)

print(reso, dreso)
