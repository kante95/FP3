import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('cid_collision_cell.txt', delimiter = '   ', skip_header = 3)
x_data = data[:, 0]

mz = np.genfromtxt('cid_collision_cell.txt', delimiter = '   ', skip_header = 2, skip_footer = 41, usecols = range(2, 44))
print(mz)

for i in range(1, 42):
    plt.plot(x_data, data[:, i], label = str(mz[i]))

plt.xlabel(r'Collision Energy in eV')
plt.ylabel(r'Intensity')
plt.legend(bbox_to_anchor = (1.1, 1.05), ncol=3)

plt.tight_layout()
#plt.savefig('cid_collision.pdf', format = 'pdf', bbox_inches = 'tight')
plt.show()