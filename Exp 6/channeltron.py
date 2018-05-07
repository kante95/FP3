import numpy as np
import matplotlib.pyplot as plt

from script import read_data,exp,V2P


for i in range(16,21):
	t1,v1 = read_data("data/ALL00"+str(i)+ "/F00"+str(i)+ "CH1.CSV")
	t2,v2 = read_data("data/ALL00"+str(i)+ "/F00"+str(i)+ "CH2.CSV")

	fig, ax1 = plt.subplots()


	ax1.plot(t1, v1, 'b-')
	ax1.set_xlabel('time [s]')
	# Make the y-axis label, ticks and tick labels match the line color.
	ax1.set_ylabel('Voltage [V]', color='b')
	ax1.tick_params('y', colors='b')

	ax2 = ax1.twinx()
	ax2.plot(t2, v2, 'g-')
	ax2.set_ylabel('Voltage [V]', color='g')
	ax2.tick_params('y', colors='g')

plt.show()