import numpy as np
import matplotlib.pyplot as plt

from mass_charge import a,b,c,x,y,z


margin = 0.5

def mz2fragment(mz):
	#horrible function, but I don't know if there is a better way
	for i in range(len(a)):
		if a[i]==mz:
			return "a"+str(i+1)
	for i in range(len(b)):
		if b[i]==mz:
			return "b"+str(i+1)
	for i in range(len(c)):
		if c[i]==mz:
			return "c"+str(i+1)
	for i in range(len(x)):
		if x[i]==mz:
			return "x"+str(i+1)
	for i in range(len(b)):
		if y[i]==mz:
			return "y"+str(i+1)
	for i in range(len(c)):
		if z[i]==mz:
			return "z"+str(i+1)

def indentifypeak(mz):
	fragments = np.concatenate((a,b,c,x,y,z))
	for i in fragments:
		if( mz-margin<i and mz+margin >i):
			print("Possible match:",mz,i)
			return i
	return False

data = np.genfromtxt('cid_collision_cell.txt', delimiter = '   ', skip_header = 3)
x_data = data[:, 0]

mz = np.genfromtxt('cid_collision_cell.txt', delimiter = '   ', skip_header = 2, skip_footer = 41, usecols = range(2, 44))
print(mz)

for i in range(1, 42):
	if(np.any(data[:,i]>5)):
		fragment = indentifypeak(mz[i])
		if(fragment):
			plt.plot(x_data, data[:, i], label = str(np.around(mz[i],decimals=2)) +" "+ mz2fragment(fragment))

plt.xlabel(r'Collision Energy (eV)')
plt.ylabel(r'Intensity')
#plt.legend(bbox_to_anchor = (1.1, 1.05), ncol=3)
plt.legend()

plt.tight_layout()
#plt.savefig('cid_collision.pdf', format = 'pdf', bbox_inches = 'tight')
plt.show()