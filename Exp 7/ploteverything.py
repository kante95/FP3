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
plt.savefig('magic_peaks.pdf', format = 'pdf')

plt.figure()

atoms = mz/19.99
area = np.zeros(14)
height = np.zeros(14)
it = (np.linspace(2, 15, 14))
for i in range(2,16):
	area[i-2] = np.trapz(y[(atoms>i-0.5)&(atoms<i+0.5)] , x = atoms[(atoms>i-0.5) &(atoms<i+0.5)])
	height[i-2] = np.amax(y[(atoms>i-0.5) & (atoms<i+0.5)])



#print(area)
plt.plot(it,area, 'gx')
plt.xlabel(r'Number of Neon atoms')
plt.ylabel(r'Area / Hz')
plt.tight_layout()
plt.savefig('magic_area.pdf', format = 'pdf')


plt.figure()
plt.plot(it, height, 'bx')
plt.xlabel(r'Number of Neon atoms')
plt.ylabel(r'Area / Hz')
plt.tight_layout()
plt.savefig('magic_height.pdf', format = 'pdf')

#Appearence energy Ne


mz, y = read_data("data/FP3_group9_calibration_I019_20p6.txt")

plt.figure()
plt.plot(mz,y)
plt.ylabel("Signal [Hz]")
plt.xlabel("Energy (eV)")


#Appearence energy Ne2

mz, y = read_data("data/FP3_group9_ne2_I01F_40p6.txt")

plt.figure()
plt.plot(mz,y)
plt.ylabel("Signal [Hz]")
plt.xlabel("Energy (eV)")


#pickup

mz, y = read_data("data/FP3_MS2_Ne13bar_air_pickup_100K_I001_70.txt")

plt.figure()
plt.plot(mz,y)
plt.ylabel("Signal [Hz]")
plt.xlabel("Energy (eV)")

plt.show()
