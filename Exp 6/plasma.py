import numpy as np
import matplotlib.pyplot as plt

from script import read_data,exp,V2P





t,v = read_data("data/ALL0013/F0013CH2.CSV")
plt.plot(t*1e6,v,label = r"width 33 $\mu$s")

t,v = read_data("data/ALL0014/F0014CH2.CSV")
plt.plot(t*1e6,v,'r',label = r"width 28 $\mu$s")

t,v = read_data("data/ALL0015/F0015CH2.CSV")
plt.plot(t*1e6,v,label = r"width 23 $\mu$s")



plt.xlabel(r"Time [$\mu$s]")
plt.ylabel("Voltage [V]")

plt.legend(loc=4)

plt.show()