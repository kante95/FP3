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
	velocity_below = 0.27/(t - start_time)
	velocity_above = 0.33/(t - start_time)
	v1 = v

	v = v[velocity_below<800]
	velocity_below =velocity_below[velocity_below< 800]
	if(file[i] == 31):
		v = v[velocity_below>180]
		velocity_below =velocity_below[velocity_below>180]
		v = v[velocity_below<500]
		velocity_below =velocity_below[velocity_below<500]
		
	else:
		v = v[velocity_below>250]
		velocity_below =velocity_below[velocity_below>250]

	v1 = v1[velocity_above<810]
	velocity_above =velocity_above[velocity_above< 810]
	if(file[i] == 31):
		v1 = v1[velocity_above>280]
		velocity_above =velocity_above[velocity_above>280]
	else:
		v1 = v1[velocity_above>350]
		velocity_above =velocity_above[velocity_above>350]

	plt.plot(velocity_below,v, label = str(width[i])+r" $\mu$s" ) 
	plt.plot(velocity_above,v1, label = str(width[i])+r" $\mu$s" ) 
		
	popt, pcov = curve_fit(floatmaxwell, velocity_below, v,method = "trf",p0=(0.01,2,350,0))
	#plt.plot(velocity,floatmaxwell(velocity_below,*popt),color="r")
	popt1, pcov1 = curve_fit(floatmaxwell, velocity_above, v1,method = "trf",p0=(0.01,2,450,0))
	#plt.plot(velocity,floatmaxwell(velocity_above,*popt1),color="r")
	perr = np.sqrt(np.diag(pcov))

	S = (np.abs(popt[1]) + np.abs(popt1[1]))/2
	dS =np.abs( (np.abs(popt[1]) - np.abs(popt1[1]))/2) 
	u = (popt[2] + popt1[2])/2
	du = np.abs((popt[2] - popt1[2])/2)
	

	plt.plot(velocity_below,floatmaxwell(velocity_below,*popt),color="r")
	plt.plot(velocity_above,floatmaxwell(velocity_above,*popt1),color="r")

	plt.xlabel("Velocity [m/s]")
	plt.ylabel("Voltage [V]")

	#print("Pressure" + str(pressure[i]))
	#plt.legend()

	soundspeed = np.sqrt((gamma*Temp)/(mk) )
	mach = u/soundspeed
	dmach = du/soundspeed
	T = (0.5*mk)*(u/S)**2
	dtdu = mk*(u/S**2)
	dtds = mk*(u**2/S**3)
	dT = np.sqrt( (dtdu*du)**2 + (dtds*dS)**2 )

	#print("Pressure | width | S | u | T | Mach")
	print(pressure[i],"&",width[i],"&", S,"\\pm",dS,"&",u,"\\pm",du,"&",T,"\\pm",dT,"&",mach,"\\pm",dmach,"\\\\")

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
v1 = v


velocity_below = 0.27/(t - start_time)
velocity_above = 0.33/(t - start_time)

v = v[velocity_below<1100]
velocity_below =velocity_below[velocity_below< 1100]
v1 = v1[velocity_above<1100]
velocity_above =velocity_above[velocity_above< 1100]


plt.plot(velocity_above,v1,label = r"230 $\mu$s") 
plt.plot(velocity_below,v,label = r"230 $\mu$s") 


popt, pcov = curve_fit(floatmaxwell, velocity_below, v,method = "trf",p0=(0.01,2,600,0))
popt1, pcov1 = curve_fit(floatmaxwell, velocity_above, v1,method = "trf",p0=(0.01,2,600,0))
perr = np.sqrt(np.diag(pcov))

S = (np.abs(popt[1]) + np.abs(popt1[1]))/2
dS =np.abs( (np.abs(popt[1]) - np.abs(popt1[1]))/2) 
u = (popt[2] + popt1[2])/2
du = np.abs((popt[2] - popt1[2])/2)


plt.plot(velocity_above,floatmaxwell(velocity_above,*popt1),color="r")
plt.plot(velocity_below,floatmaxwell(velocity_below,*popt),color="r")
plt.xlabel("Velocity [m/s]")
plt.ylabel("Voltage [V]")


soundspeed = np.sqrt((gamma*Temp)/(mk) )
mach = u/soundspeed
dmach = du/soundspeed
T = (0.5*mk)*(u/S)**2
dtdu = mk*(u/S**2)
dtds = mk*(u**2/S**3)
dT = np.sqrt( (dtdu*du)**2 + (dtds*dS)**2 )

print(230,"&", S,"\\pm",dS,"&",u,"\\pm",du,"&",T,"\\pm",dT,"&",mach,"\\pm",dmach,"\\\\")

###################################################à
t,v = read_data("data/ALL0037/F0037CH1.CSV")

for k in v:
		if k < 0.0004:
			start_time = k
			break
v = -v
v = v[t>start_time]
t = t[t>start_time]
v1 = v


velocity_below = 0.27/(t - start_time)
velocity_above = 0.33/(t - start_time)

v = v[velocity_below<1100]
velocity_below =velocity_below[velocity_below< 1100]
v1 = v1[velocity_above<1100]
velocity_above =velocity_above[velocity_above< 1100]

plt.plot(velocity_below,v,label = r"220 $\mu$s") 
plt.plot(velocity_above,v1,label = r"220 $\mu$s") 
popt, pcov = curve_fit(floatmaxwell, velocity_below, v,method = "trf",p0=(0.01,2,600,0))
popt1, pcov1 = curve_fit(floatmaxwell, velocity_above, v1,method = "trf",p0=(0.01,2,600,0))
perr = np.sqrt(np.diag(pcov))

S = (np.abs(popt[1]) + np.abs(popt1[1]))/2
dS =np.abs( (np.abs(popt[1]) - np.abs(popt1[1]))/2) 
u = (popt[2] + popt1[2])/2
du = np.abs((popt[2] - popt1[2])/2)

plt.plot(velocity_below,floatmaxwell(velocity_below,*popt),color="r")
plt.plot(velocity_above,floatmaxwell(velocity_above,*popt1),color="r")

soundspeed = np.sqrt((gamma*Temp)/(mk) )
mach = u/soundspeed
dmach = du/soundspeed
T = (0.5*mk)*(u/S)**2
dtdu = mk*(u/S**2)
dtds = mk*(u**2/S**3)
dT = np.sqrt( (dtdu*du)**2 + (dtds*dS)**2 )

print(220,"&", S,"\\pm",dS,"&",u,"\\pm",du,"&",T,"\\pm",dT,"&",mach,"\\pm",dmach,"\\\\")

plt.legend()

plt.show()