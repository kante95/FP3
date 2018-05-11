import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import signal

plt.rcParams['font.size'] = 16



def read_data(file):
    data = np.genfromtxt(file, delimiter=",",usecols=range(3,5), skip_header=18)
    return data[:,0],data[:,-1]

def exp(t,tau,A,B,C):
	return A*np.exp(-(t+B)/tau) +C

def V2P(v, gas = "argon"):
	if gas == "argon":
		k = 0.8
	elif gas =="helium":
		k = 5.9
	return k*10**(1.667*v - 9.333)



if __name__ == "__main__":
	
	#pressure for different opening times
	width = [150,120,190,230]
	for i in range(0,4):
		#plt.figure()
		t,v = read_data("data/ALL000"+str(i)+"/F000"+str(i)+"CH1.CSV")
		plt.plot(t,V2P(v),label = str(width[i]) + r" $\mu$S")
		plt.xlabel("Time [s]")
		plt.ylabel("Pressure [Pa]")

	plt.legend()

	#pressure for different frequencies

	plt.figure()
	freq = [1,2,5,10]

	num = [1,6,7,12]
	j=0
	for i in num:
		#plt.figure()
		t,v = read_data("data/ALL00"+str(i).zfill(2) +"/F00"+str(i).zfill(2) +"CH1.CSV")
		plt.plot(t,V2P(v),label = str(freq[j]) + " Hz")
		plt.xlabel("Time [s]")
		plt.ylabel("Pressure [Pa]")
		j+=1

	plt.legend()


	#knudsen number

	def knudsen(p):
		kb = 1.3806504e-23
		T = 22 + 273.15
		d = 3.4e-10
		L = 0.35
		return kb*T/(np.sqrt(2)*np.pi*d**2*p*L)

	fig, ax1 = plt.subplots()


	t,v = read_data("data/ALL0002/F0002CH1.CSV")
	p = V2P(v)
	ax1.plot(t, p, 'b-')
	ax1.set_xlabel('time [s]')
	# Make the y-axis label, ticks and tick labels match the line color.
	ax1.set_ylabel('Pressure [Pa]', color='b')
	ax1.tick_params('y', colors='b')

	p = p[(t>0) &(t<0.4)]
	t = t[(t>0)& (t<0.4)]
	ax2 = ax1.twinx()
	s2 = knudsen(p)
	ax2.plot(t, s2, 'g.')
	ax2.set_ylabel('Knudsen number', color='g')
	ax2.tick_params('y', colors='g')

	print("Knudsen min:",np.amin(s2))

	#gas inlet
	V_final = 4
	gamma = 5/3
	P_initial = 2.9


	freq = np.array([1,1,1,2,2,2,5,5,5,10,10,10])
	width = np.array([120,190,230,230,190,120,120,190,230,230,190,120])

	gasquantity = np.zeros(len(freq))
	print("Gas inlet")

	for i in range(1,13):
		t,v = read_data("data/ALL00"+str(i).zfill(2) +"/F00"+str(i).zfill(2) +"CH1.CSV")
		p = V2P(v)
		P_final = np.amax(p)*1e-5
		V_initial = V_final*(P_final/P_initial)*1e3 #milliliters
		gasquantity[i-1] = V_initial
		print(str(V_initial)+" +/- " +str((P_final/P_initial)*1e3) + "& " +str(width[i-1])+ "& " +str(freq[i-1]))



	#decay fit

	freq = np.array([1,1,1,2,2,2,5,5,5])
	width = np.array([120,190,230,230,190,120,120,190,230])

	tau = np.zeros(len(freq)+3)

	for i in range(1,10):
		t,v = read_data("data/ALL00"+str(i).zfill(2) +"/F00"+str(i).zfill(2) +"CH1.CSV")
		p = V2P(v)
		cut = np.argmax(p)
		#print(t[cut])
		cut_lower = t[cut]
		cut_upper = t[cut]+ 0.5*(1/freq[i-1])
		p = p[(t>cut_lower)&(t<cut_upper)]
		t = t[ (t>cut_lower)&(t<cut_upper)]
		popt, pcov = curve_fit(exp, t, p,method = "trf",p0 = [0.1,1,1,1])
		perr = np.sqrt(np.diag(pcov))
		plt.figure()
		plt.plot(t,p)
		plt.plot(t, exp(t, *popt), 'r')
		plt.title("width: "+str(width[i-1]) + ", freq: " + str(freq[i-1]))
		print("width: "+str(width[i-1]) + ", freq: " + str(freq[i-1])+" tau: " +str(popt[0]) + " +/- " + str(perr[0]))
		plt.xlabel("Time [s]")
		plt.ylabel("Pressure [Pa]")
		tau[i-1] = popt[0]

	tau[2] = 0.0567
	tau[3] = 0.0556
	tau[-1] = 0.28
	tau[-2] = 0.19
	tau[-3] = 0.17


	print(gasquantity)
	plt.figure()
	plt.plot(gasquantity,tau,'o')
	plt.xlabel("Gas inlet [mL]")
	plt.ylabel("Time scale [s]")










	#time of flight

	plt.figure()

	for i in range(21,24):
		t,v = read_data("data/ALL00"+str(i).zfill(2) +"/F00"+str(i).zfill(2) +"CH1.CSV")
		#peak_indices = signal.find_peaks_cwt(-1*v,np.arange(1,2))
		#print(peak_indices)
		plt.plot(t,v)
		ind1 = np.argmin(v[t<0.0005])
		ind2 = np.argmin(v[t>0.0005])
		plt.plot(t[ind1],v[ind1],'r.')
		plt.plot(t[ind2 + len(v)-len(v[t>0.0005]) ],v[ind2+ len(v)-len(v[t>0.0005])],'r.')

		tof = t[ind2 + len(v)-len(v[t>0.0005])]-t[ind1]
		print("time fo flight: ",tof, " Velocity: ",0.35/tof)
	plt.show()