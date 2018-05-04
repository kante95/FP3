import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['font.size'] = 16



def read_data(file):
    data = np.genfromtxt(file, delimiter=",",usecols=range(3,5), skip_header=18)
    return data[:,0],data[:,-1]


def V2P(v, gas = "argon"):
	if gas == "argon":
		k = 0.8
	elif gas =="helium":
		k = 5.9
	return k*10**(1.667*v - 9.333)


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



#gas inlet
V_final = 4
gamma = 5/3
P_initial = 2.9


freq = np.array([1,1,1,2,2,2,5,5,5,10,10,10])
width = np.array([120,190,230,230,190,120,120,190,230,230,190,120])


for i in range(1,13):
	t,v = read_data("data/ALL00"+str(i).zfill(2) +"/F00"+str(i).zfill(2) +"CH1.CSV")
	p = V2P(v)
	P_final = np.amax(p)*1e-5
	V_intial = V_final*(P_final/P_initial)**(1/gamma)*1e3
	print("Gas inlet: "+str(V_intial)+" +/- " +str((P_final/P_initial)**(1/gamma)*1e3) + " mBar, Freq: " +str(freq[i-1])+ " Width: " +str(width[i-1]))



#plt.show()