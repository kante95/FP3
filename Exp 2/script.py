import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import signal


plt.rcParams['font.size'] = 16



def read_data(file):
    data = np.genfromtxt(file, delimiter=",",usecols=range(0,2), skip_header=1)
    return data[:,0],data[:,-1]


#reference
t, ch1 = read_data("data/PID01.CSV")
t, ch2 = read_data("data/PID02.CSV")


plt.plot(t,ch1)

#plt.figure()
#plt.plot(t,ch2)

peaks = np.array([])
for i in range(len(ch1)-1):
	if ch1[i]> 0.03:
		if ch1[i]>ch1[i+1] and ch1[i]>ch1[i-1]:
			#plt.plot(t[i],ch1[i],'ro')
			peaks = np.append(peaks,t[i])

plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.grid(True)



distance = np.abs(peaks[-1] - peaks[-3])
t2v = 1.1/distance #peaks are separeted by 1.1 Ghz, this factor gives the conversion between time and frequency


#P controler
t,ch1 = read_data("data/PID03.CSV")
#plt.figure()
#plt.plot(t,ch1)
print("Division P: ", (max(t)-min(t))/10 )

#PI controler
t,ch1 = read_data("data/PID04.CSV")
#plt.figure()
#plt.plot(t,ch1)
print("Division PI: ", (max(t)-min(t))/10 )

#PID controler
t,ch1 = read_data("data/PID05.CSV")
#plt.figure()
#plt.plot(t,ch1)
print("Division PID: ", (max(t)-min(t))/10 )

plt.show() 


division = 1e-3 #1 millisecond

full_widths = np.array([48,19.5,28])

time = full_widths/50 # 1 division is 1 ms and 50 pixel, so time in ms

freq = t2v*(time*1e-3) # result in GHz

print("Frequency shifts: ",freq," GHz")