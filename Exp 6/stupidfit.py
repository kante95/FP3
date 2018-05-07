import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from script import read_data,exp,V2P


#decay fit


#freq 1 width 230


t,v = read_data("data/ALL0003/F0003CH1.CSV")
p = V2P(v)
cut = np.argmax(p)
#print(t[cut])
cut_lower = t[cut] + 0.03
cut_upper = t[cut]+ 0.5
p = p[(t>cut_lower)&(t<cut_upper)]
t = t[ (t>cut_lower)&(t<cut_upper)]
popt, pcov = curve_fit(exp, t, p,method = "trf",p0 = [0.1,1,1,1])
perr = np.sqrt(np.diag(pcov))
plt.figure()
plt.plot(t,p)
plt.plot(t, exp(t, *popt), 'r')
print("width:230 freq: 1 tau: " +str(popt[0]) + " +/- " + str(perr[0]))
plt.xlabel("Time [s]")
plt.ylabel("Pressure [Pa]") 



t,v = read_data("data/ALL0004/F0004CH1.CSV")
p = V2P(v)
cut = np.argmax(p)
#print(t[cut])
cut_lower = t[cut] + 0.03
cut_upper = t[cut]+ 0.4
p = p[(t>cut_lower)&(t<cut_upper)]
t = t[ (t>cut_lower)&(t<cut_upper)]
popt, pcov = curve_fit(exp, t, p,method = "trf",p0 = [0.1,1,1,1])
perr = np.sqrt(np.diag(pcov))
plt.figure()
plt.plot(t,p)
plt.plot(t, exp(t, *popt), 'r')
print("width:230 freq: 2 tau: " +str(popt[0]) + " +/- " + str(perr[0]))
plt.xlabel("Time [s]")
plt.ylabel("Pressure [Pa]") 




#10 HZ

for i in range(10,13):
	t,v = read_data("data/ALL00"+str(i) + "/F00"+str(i) + "CH1.CSV")
	p = V2P(v)
	#cut = np.argmax(p)
	#print(t[cut])
	#cut_lower = t[cut] + 0.03
	cut_upper = t[0]+ 0.07
	p = p[(t<cut_upper)]
	t = t[(t<cut_upper)]
	popt, pcov = curve_fit(exp, t, p,method = "trf",p0 = [0.05,1,1,1])
	perr = np.sqrt(np.diag(pcov))
	plt.figure()
	plt.plot(t,p)
	plt.plot(t, exp(t, *popt), 'r')
	print("width:roba freq: 10 tau: " +str(popt[0]) + " +/- " + str(perr[0]))
	plt.xlabel("Time [s]")
	plt.ylabel("Pressure [Pa]") 


plt.show()