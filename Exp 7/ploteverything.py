import numpy as np 
import matplotlib.pyplot as plt 


def read_data(file):
    data = np.genfromtxt(file, delimiter="\t",usecols=range(0,2))
    return data[:,0],data[:,-1]


#Isotope spectrum

mz, y = read_data("data/FP3_group9_isotopeneon1_I007_70.txt")

plt.plot(mz,y)
plt.ylabel("Signal [Hz]")
plt.xlabel("M/z")




#Magic numbers

mz, y = read_data("data/FP3_group9_magicnumbers_I007_70.txt")

plt.figure()
plt.plot(mz,y)
plt.ylabel("Signal [Hz]")
plt.xlabel("M/z")


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