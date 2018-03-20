import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from scipy import signal


N =20


def read_data(file):
    data = np.genfromtxt(file, delimiter=",",usecols=range(0,2), skip_header=1)
    return data[:,0],data[:,-1]

def cut_data(t,v,low,high):
	v = v[(t> low) & (t< high)]
	t = t[(t> low) & (t< high)]
	return t,v

def nice_data(c,v):
	#sorting 
	p = c.argsort()
	c = c[p]
	v = v[p]
	#mean over 10 point
	new_c = np.array([])
	new_v = np.array([])
	for i in range(len(c)-10):
		new_c = np.append(new_c,np.mean(c[i:i+10]))
		new_v = np.append(new_v,np.mean(v[i:i+10]))
	return new_c,new_v

t1, current = read_data("data/MARCO_24.CSV")
t2, voltage = read_data('data/MARCO_23.CSV')


current,voltage = nice_data(current,voltage)

plt.figure()

current,p = np.unique(current,return_index=True)
voltage = voltage[p]
#np.set_printoptions(threshold=np.inf)
#print(np.diff(current)!=0)
plt.plot(current,voltage)

derivative = np.gradient(voltage,current)

#plt.figure()
#plt.plot(current,derivative)

#peakind = signal.find_peaks_cwt(derivative, np.arange(1,10))
#plt.plot(current[peakind],derivative[peakind],'ro')
#for i in range(len(derivative)-1):
#	if(derivative[i]*derivative[i+1]<0):
#		plt.plot(current[i],voltage[i],'ro')

spl = UnivariateSpline(current,voltage,k=5)
spl.set_smoothing_factor(0.1)

print(spl.get_coeffs())

r = spl.derivative(2).roots()

plt.plot(r, spl(r), 'ro')
plt.plot(current,spl(current))


plt.grid(True)
plt.ylabel("Voltage [mV]")
plt.xlabel("Current [mA]")
plt.show() 
