import numpy as np
import matplotlib.pyplot as plt

from mass_charge import a,b,c,x,y,z


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

def identifypeak(mz,margin=0.5):
	fragments = np.concatenate((a,b,c,x,y,z))
	for i in fragments:
		if( mz-margin<i and mz+margin >i):
			print("Possible match:",mz,i)
			return i
	return False 
