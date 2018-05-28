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


#Isotope spectrum

mz, y = read_data("data/FP3_group9_isotopeneon1_I007_70.txt")

plt.plot(mz,y)
plt.ylabel("Signal [Hz]")
plt.xlabel("M/z")
#plt.xlim(38,44)


#Magic numbers

mz, y = read_data("data/FP3_group9_magicnumbers_I007_70.txt")

plt.figure()
plt.plot(mz/20,y)



plt.ylabel("Signa [Hz]")
plt.xlabel("Neon atoms #")


plt.figure()

atoms = mz/20.1797
for i in range(1,16):
	area = np.trapz(y[(atoms>i-0.5)&(atoms<i+0.5)] , x = atoms[(atoms>i-0.5) &(atoms<i+0.5)])
	#print(area)
	plt.plot(i,area)

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