import numpy as np
import matplotlib.pyplot as plt
#import lmfit.model as lm
import scipy.optimize as sp

import matplotlib
matplotlib.rc('text', usetex = True)
params = {'text.latex.unicode':True, 'text.latex.preamble': [r'\usepackage{siunitx}']}
plt.rcParams.update(params)

N = 10

def linear_function(x, a, b):
    return a * x + b

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


#tI = np.genfromtxt('data/MARCO_11.CSV', delimiter=",",usecols=range(0), skip_header=1)

tI, current = read_data('data/MARCO_11.CSV')
tU, voltage = read_data('data/MARCO_12.CSV')

current, voltage, dI, dU = nice_data(current, voltage)

low = 0.63
high= 0.67

I_fit = current[(current < high) & (current > low)]
U_fit = voltage[(current < high) & (current > low)]
dI_fit= dI[(current < high) & (current > low)]
dU_fit= dU[(current < high) & (current > low)]

high2= 0.3
low2 = -0.3

I_fit2 = current[(current < high2) & (current > low2)]
U_fit2 = voltage[(current < high2) & (current > low2)]
dI_fit2= dI[(current < high2) & (current > low2)]
dU_fit2= dU[(current < high2) & (current > low2)]

params, cov = sp.curve_fit(linear_function, I_fit, U_fit, sigma = dU_fit)
print(params)

params2, cov2 = sp.curve_fit(linear_function, I_fit2, U_fit2, sigma = dU_fit2)
print(params2)
x = np.linspace(0.5, 0.7)

intersection = (params2[1] - params[1]) / (params[0] - params2[0])
print(intersection)

plt.plot(current, voltage, color = 'k')
plt.plot(x, linear_function(x, *params), color = 'r')
plt.plot(x, linear_function(x, *params2), color = 'b')
plt.errorbar(intersection, linear_function(intersection, *params), color = 'k', fmt = 'x')
#plt.plot(tI, current)
plt.ylabel(r'$V$ / \si{\micro \volt}')
plt.xlabel(r'$I$ / \si{\micro \ampere}')
#plt.xlim(0.25)
#plt.ylim(0)
plt.show()
