import numpy as np
import matplotlib.pyplot as plt
#import lmfit.model as lm
import scipy.optimize as sp

import matplotlib
matplotlib.rc('text', usetex = True)
params = {'text.latex.unicode':True, 'text.latex.preamble': [r'\usepackage{siunitx}']}
plt.rcParams.update(params)

N = 10

def sine_function(x, a, b, c, d):
    return a * np.sin(b * x + c) + d

def read_data(file):
    data = np.genfromtxt(file, delimiter=",",usecols=range(0,2), skip_header=1)
    return data[:,0], data[:,-1]
    
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

tI, current = read_data('data/MARCO_17.CSV')
tU, voltage = read_data('data/MARCO_18.CSV')

current, voltage, dI, dU = nice_data(current, voltage)

low = -0.46
high= 3.66

# The *100 transforms the values into micro amps/micro volts
I_fit = current[(current < high) & (current > low)]*100
U_fit = voltage[(current < high) & (current > low)]*100
dI_fit= dI[(current < high) & (current > low)]*100
dU_fit= dU[(current < high) & (current > low)]*100

params, cov = sp.curve_fit(sine_function, I_fit, U_fit, p0 = [2.5, np.pi/50, np.pi, 18.2], sigma = dU_fit)
dparams = np.sqrt(np.diag(cov))
print(params)
print(dparams)

plt.plot(I_fit, U_fit, color = 'k')
plt.plot(I_fit, sine_function(I_fit, *params), color = 'r')
plt.xlabel(r'$I_{Coil}$ / \si{\micro \ampere}', fontsize = 'large')
plt.ylabel(r'$V$ / \si{\micro \volt}', fontsize = 'large')
#plt.savefig('v_flux.pdf', format = 'pdf')
plt.show()

