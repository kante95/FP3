import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from scipy import signal
from scipy.optimize import curve_fit

N = 10

def distance(x,y,x1,y1):
	return np.sqrt((x-x1)**2+(y-y1)**2)

def line(x,a,b):
	return a*x+b

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
	dc = np.array([])
	dv = np.array([])
	for i in range(int(len(c)/N)-N):
		new_c = np.append(new_c,np.mean(c[N*i:N*i+N]))
		new_v = np.append(new_v,np.mean(v[N*i:N*i+N]))
		dc = np.append(dc,np.std(c[N*i:N*i+N]))
		dv = np.append(dv,np.std(v[N*i:N*i+N]))
	return new_c,new_v,dc,dv


freq = np.array([15,20,11,13,17]) #GHz
files_ch2 = np.array([23,26,28,30,32])
files_ch1 = np.array([24,25,27,29,31])
n_steps = np.array([4,2,2,1,3])
lower_step = np.array([3,6,4,4,4],dtype= np.int32)-1
higher_step = np.array([11,10,6,6,10],dtype= np.int32)-1

steps_heigth = np.zeros(len(freq))
dsteps_heigth = np.zeros(len(freq))


for k in range(len(freq)):
	t1, current = read_data("data/MARCO_"+str(files_ch1[k])+".CSV")
	t2, voltage = read_data("data/MARCO_"+str(files_ch2[k])+".CSV")


	current,voltage,dc,dv = nice_data(current,voltage)

	plt.figure(str(freq[k])+ " GHz")

	current,p = np.unique(current,return_index=True)
	voltage = voltage[p]
	dc = dc[p]
	dv = dv[p]

	plt.errorbar(current,voltage, xerr=dc , yerr=dv,fmt='-')

	spl = UnivariateSpline(current,voltage,k=5)
	spl.set_smoothing_factor(0.1)

#print(spl.get_coeffs())

	r = spl.derivative(2).roots()

#closest point?



	best_index = np.array([])
	for j in r:
		best = 10000000000
		index = 0
		for i in range(len(current)):
			d = distance(current[i],voltage[i],j,spl(j))
			if(d<best):
				best = d
				index =i
		best_index = np.append(best_index,index)

	print(best_index)
	for i in best_index:
		plt.plot(current[int(i)],voltage[int(i)],'ro')

	if(k!=0):
		steps_heigth[k] = (voltage[int(best_index[higher_step[k]])] - voltage[int(best_index[lower_step[k]])] )/n_steps[k]
		dsteps_heigth[k] = (np.sqrt(dv[int(best_index[higher_step[k]])]**2 + dv[int(best_index[lower_step[k]])]**2))/n_steps[k] #negletting horizontal error wicch should be 0
	else:
		steps_heigth[k] = (voltage[int(best_index[higher_step[k]] )] - voltage[int(best_index[lower_step[k]])] )/n_steps[k]
		dsteps_heigth[k] = (np.sqrt(dv[int(best_index[higher_step[k]])]**2 + dv[int(best_index[lower_step[k]])]**2))/n_steps[k]
#plt.plot(r, spl(r), 'ro')
#plt.plot(current,spl(current))


	plt.grid(True)
	plt.ylabel("Voltage [mV]")
	plt.xlabel("Current [mA]")

plt.figure()
plt.errorbar(freq,steps_heigth,yerr=dsteps_heigth,fmt='.')
plt.ylabel("Step height [mV]")
plt.xlabel("Frequency [GHz]")


#

freq = np.delete(freq, 1)
steps_heigth = np.delete(steps_heigth, 1)
dsteps_heigth = np.delete(dsteps_heigth,1)
popt, pcov = curve_fit(line,freq,steps_heigth,sigma=dsteps_heigth)
eh = 2*popt[0]

f = np.linspace(10,20,10000)
plt.plot(f,line(f,*popt))
plt.grid(True)

deh = np.sqrt(np.diag(pcov))[0]
print("Value of h/e = ", 1/eh,deh*(1/eh)**2)

print(freq/(2*steps_heigth))

plt.show() 
