import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


from script import read_data,exp,V2P


u2M =  1.660539040e-27
m = 39.948*u2M # amu
k = 1.38064852e-23

mk =  m/k

gamma = 5/3

Temp = 22 + 273.15

def floatmaxwell(v,C,S,u,off):
	return C*v**2*np.exp(-S**2*(1-v/u)**2) + off
#time of flight

width = np.array([210,220,230,230,220,210,210,220,230,210,220,230])
file = np.array([22,23,24,25,26,27,29,30,31,32,33,34])
pressure = np.array([1.9,1.9,1.9,2.1,2.1,2.1,1.7,1.7,1.7,1.5,1.5,1.5])
for i in range(len(file)):
	if i==0:
		plt.figure() 
	elif pressure[i] != pressure[i-1]:
		plt.figure() 
	t,v = read_data("data/ALL00"+str(file[i]).zfill(2) +"/F00"+str(file[i]).zfill(2) +"CH1.CSV")
	#peak_indices = signal.find_peaks_cwt(-1*v,np.arange(1,2))
	#print(peak_indices)
	for k in v:
		if k < 0.0003:
			start_time = k
			break
	v = -v
	v = v[t>start_time]
	t = t[t>start_time]
	velocity = 0.3/(t - start_time)

	v = v[velocity<800]
	velocity =velocity[velocity< 800]
	if(file[i] == 31):
		v = v[velocity>280]
		velocity =velocity[velocity>280]
	else:
		v = v[velocity>350]
		velocity =velocity[velocity>350]

	plt.plot(velocity,v, label = str(width[i])+r" $\mu$s" ) 
		
	popt, pcov = curve_fit(floatmaxwell, velocity, v,method = "trf",p0=(0.01,2,450,0))
	perr = np.sqrt(np.diag(pcov))

	S = np.abs(popt[1])
	u = popt[2]
	plt.plot(velocity,floatmaxwell(velocity,*popt),color="r")

	plt.xlabel("Velocity [m/s]")
	plt.ylabel("Voltage [V]")

	#print("Pressure" + str(pressure[i]))
	plt.legend()

	soundspeed = np.sqrt((gamma*Temp)/(mk) )
	mach = u/soundspeed
	T = (0.5*mk)*(u/S)**2

	#print("Pressure | width | S | u | T | Mach")
	print(pressure[i],"&",width[i],"&", S,"&", u,"&",T,"&",mach,"\\\\")

#helium pressure 2.5

print("Helium")
plt.figure()
t,v = read_data("data/ALL0036/F0036CH1.CSV")

for k in v:
		if k < 0.0003:
			start_time = k
			break
v = -v
v = v[t>start_time]
t = t[t>start_time]

velocity = 0.3/(t - start_time)
v = v[velocity<2000]
velocity =velocity[velocity< 2000]

plt.plot(velocity,v,label = r"230 $\mu$s") 
popt, pcov = curve_fit(floatmaxwell, velocity, v,method = "trf",p0=(0.01,2,600,0))
perr = np.sqrt(np.diag(pcov))

S = np.abs(popt[1])
u = popt[2]
plt.plot(velocity,floatmaxwell(velocity,*popt),color="r")
plt.xlabel("Velocity [m/s]")
plt.ylabel("Voltage [V]")


soundspeed = np.sqrt((gamma*Temp)/(mk) )
mach = u/soundspeed
T = (0.5*mk)*(u/S)**2

print(230, S, u,T,mach)

###################################################à
t,v = read_data("data/ALL0037/F0037CH1.CSV")

for k in v:
		if k < 0.0004:
			start_time = k
			break
v = -v
v = v[t>start_time]
t = t[t>start_time]
velocity = 0.3/(t - start_time)
v = v[velocity<2000]
velocity =velocity[velocity< 2000]
plt.plot(velocity,v,label = r"220 $\mu$s") 
popt, pcov = curve_fit(floatmaxwell, velocity, v,method = "trf",p0=(0.01,2,600,0))
perr = np.sqrt(np.diag(pcov))

S = np.abs(popt[1])
u = popt[2]
plt.plot(velocity,floatmaxwell(velocity,*popt),color="r")

soundspeed = np.sqrt((gamma*Temp)/(mk) )
mach = u/soundspeed
T = (0.5*mk)*(u/S)**2

print(220, S, u,T,mach)
plt.legend()

plt.show()