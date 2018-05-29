import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema


plt.rcParams['font.size'] = 16

def read_data(file):
    data = np.genfromtxt(file, delimiter="\t",usecols=range(0,2))
    return data[:,0],data[:,-1]



m20 = 19.9924401754
m21 = 20.99384668
m22 = 21.991385114


#Isotope 8spectrum

mz, y = read_data("data/FP3_group9_isotopeneon1_I007_70.txt")

plt.plot(mz,y)
plt.ylabel("Signal [Hz]")
plt.xlabel("M/z")
#plt.xlim(38,44)


#Magic numbers

mz, y = read_data("data/FP3_group9_magicnumbers_I007_70.txt")

plt.figure(figsize=(12, 6))
plt.plot(mz/19.99,y)



plt.ylabel(r"Intensity / Hz")
plt.xlabel("Number of Neon atoms in cluster")
plt.tight_layout()
#plt.savefig('magic_peaks.pdf', format = 'pdf')



atoms = (mz - 0.5)/19.99
area = np.zeros(14)
height = np.zeros(14)
it = (np.linspace(2, 15, 14))
for i in range(2,16):
	area[i-2] = np.trapz(y[(atoms>i-0.5)&(atoms<i+0.5)] , x = atoms[(atoms>i-0.5) &(atoms<i+0.5)])
	height[i-2] = np.amax(y[(atoms>i-0.5) & (atoms<i+0.5)])
plt.figure()
#print(area)
plt.plot(it,area, 'gx')
plt.xlabel(r'Number of Neon atoms')
plt.ylabel(r'Area / Hz')
plt.tight_layout()
#plt.savefig('magic_area.pdf', format = 'pdf')


plt.figure()
plt.plot(it, height, 'bx')
plt.xlabel(r'Number of Neon atoms')
plt.ylabel(r'Area / Hz')
plt.tight_layout()
#plt.savefig('magic_height.pdf', format = 'pdf')

#Appearence energy Ne

import scipy.optimize as sp

def constant_function(x, a):
	return a * np.ones(len(x))

def linear_function(x, a, b):
	return a * x + b

energy, y = read_data("data/FP3_group9_calibration_I019_20p6.txt")

params, cov = sp.curve_fit(constant_function, energy[energy<20.3], y[energy<20.3])
dparams = np.sqrt(np.diag(cov))
print(params[0])
print(dparams[0])

params2, cov2 = sp.curve_fit(linear_function, energy[(energy>20.6) & (energy<21.2)], y[(energy>20.6) & (energy<21.2)])
dparams2 = np.sqrt(np.diag(cov2))
print(params2[0], params2[1])
print(dparams2[0], dparams2[1])

intersection = (params[0] - params2[1]) / (params2[0])
dintersection= 1/(params2[0]) * np.sqrt(dparams2[1]**2 + dparams[0]**2 + ( (dparams2[0]**2 * (params[0] - params2[1])**2) / (params2[0])**2) + 2 * (params[0] - params2[1]) / (params2[0]) * cov2[1][0])
print(intersection, dintersection)

x1 = np.linspace(19,21,2)
x2 = np.linspace(20.2,22,2)

plt.figure(figsize = (10, 6))
plt.plot(energy,y)
plt.plot(x1, constant_function(x1, *params))
plt.plot(x2, linear_function(x2, *params2))
plt.ylabel("Intensity / Hz")
plt.xlabel("Electron energy / eV")
plt.tight_layout()
#plt.savefig('energy_ne.pdf', format = 'pdf')


#Appearence energy Ne2

energy, y = read_data("data/FP3_group9_ne2_I01F_40p6.txt")
a = - intersection + 21.56454
energy = energy + a

params, cov = sp.curve_fit(constant_function, energy[energy<20.3+a], y[energy<20.3+a])
dparams = np.sqrt(np.diag(cov))
print(params[0])
print(dparams[0])

params2, cov2 = sp.curve_fit(linear_function, energy[(energy>20.6+a) & (energy<21.2+a)], y[(energy>20.6+a) & (energy<21.2+a)])
print(cov2)
dparams2 = np.sqrt(np.diag(cov2))
print(params2[0], params2[1])
print(dparams2[0], dparams2[1])


intersection = (params[0] - params2[1]) / (params2[0])
dintersection= 1/(params2[0]) * np.sqrt(dparams2[1]**2 + dparams[0]**2 + ( (dparams2[0]**2 * (params[0] - params2[1])**2) / (params2[0])**2) + 2 * (params[0] - params2[1]) / (params2[0]) * cov2[1][0])
print(intersection, dintersection)

x1 = np.linspace(19,21,2)
x2 = np.linspace(20.2,22,2)

plt.figure(figsize = (10, 6))
plt.plot(energy,y)
plt.plot(x1+a, constant_function(x1+a, *params))
plt.plot(x2+a, linear_function(x2+a, *params2))
plt.ylabel("Intensity / Hz")
plt.xlabel("Electron energy / eV")
plt.tight_layout()
#plt.savefig('energy_ne2.pdf', format = 'pdf')




#pickup

mz, y = read_data("data/FP3_MS2_Ne13bar_air_pickup_100K_I001_70.txt")

plt.figure()
plt.plot(mz,y)
plt.ylabel("Signal [Hz]")
plt.xlabel("M/z ")

plt.show()
