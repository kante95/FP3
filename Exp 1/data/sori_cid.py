import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('sori_cid.txt', delimiter = '   ', skip_header = 3)
x_data = np.linspace(0, 3, 7)

mz = np.genfromtxt('sori_cid.txt', delimiter = '   ', skip_header = 2, skip_footer = 7, usecols = range(1, 29))

for i in range(1, 28):
    plt.plot(x_data, data[:, i], label = str(mz[i]))

plt.xlabel(r'SORI Energy in %')
plt.ylabel(r'Intensity')
plt.legend(bbox_to_anchor = (1.1, 1.05), ncol=2)
plt.tight_layout()
#plt.savefig('sori_cid.pdf', format = 'pdf', bbox_inches = 'tight')
plt.show()
