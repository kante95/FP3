import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from scipy.optimize import curve_fit
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes,mark_inset


plt.rcParams['font.size'] = 16

def read_data(file):
    data = np.genfromtxt(file, delimiter=",",usecols=range(0,2), skip_header=1)
    return data[:,0],data[:,-1]

def cut_data(t,v,low,high):
	v = v[(t> low) & (t< high)]
	t = t[(t> low) & (t< high)]
	return t,v

def line(x,a,b):
	return a*x+b


def v2temp(v):
	return -0.371*v+446.18

voltages = np.array([505,533,613,701.6,788.0,854.9,887.5,903.2,919.0,931,943.0,952.2,960.4,967.7,971.3,995.2])
#t1, current = read_data("temperature/MARCO_33.CSV")
#t2, voltage = read_data('temperature/MARCO_34.CSV')

R = np.array([])
dR = np.array([])

for i in range(33,64,2):
	t1, current = read_data("temperature/MARCO_"+str(i)+ ".CSV")
	t2, voltage = read_data('temperature/MARCO_'+str(i+1)+ '.CSV')
	current,voltage = cut_data(current,voltage,-0.04,0.04)
	#plt.figure(v2temp(voltages[int((i-33)/2)]))
	#plt.plot(0.1*current,0.1*voltage,zorder=10)
	popt, pcov = curve_fit(line,current, voltage)
	resistance = popt[0]#(voltage[300]-voltage[100])/(current[300]-current[100])
	R = np.append(R,resistance)
	dR = np.append(dR,np.sqrt(np.diag(pcov))[0] )
	#plt.plot(0.1*current,0.1*line(current,*popt))
	#plt.xlabel("Current [mA]")
	#plt.ylabel("Voltage [mV]")
	#plt.grid(True)
	#print(resistence)

print("dati:", v2temp(voltages),R,dR)

plt.figure()
plt.errorbar(v2temp(voltages),R,yerr=dR,xerr=0.3*0.371,fmt='.')
plt.grid(True)
plt.xlabel("Temperature [K]")
plt.ylabel(r"Resistance [$\Omega$]")


popt, pcov = curve_fit(line,v2temp(voltages)[0:-4], R[0:-4],sigma=dR[0:-4])

plt.plot(v2temp(voltages)[0:-4], line(v2temp(voltages)[0:-4],*popt))

print(popt)
perr = np.sqrt(np.diag(pcov))
print(perr)



#plt.grid(True)
#.xlabel("Temperature [K]")
#plt.ylabel(r"Resistance [$\Omega$]")



plt.show() 
 
