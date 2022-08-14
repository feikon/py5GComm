import matplotlib.pyplot as plt
import numpy as np

from PathLossModel.PathLoss import freeSpacePathloss, getLamda


def plotFreeSpacePathloss(frequency):
	lamda = getLamda(frequency)
	dList = np.arange(0.1, 100, 1)
	pathloss = []
	for d in dList:
		pathlossValue = freeSpacePathloss(d, lamda)
		pathloss.append(pathlossValue)
	plt.xlabel('Distance(Unit:m)')
	plt.ylabel('Pathloss(Unit:dB)')
	plt.title('Free space pathloss')
	plt.plot(dList, pathloss, label=str(frequency / 1e6) + 'MHz')
	plt.legend()


if __name__ == '__main__':
	plotFreeSpacePathloss(2565e6)
	plotFreeSpacePathloss(3450e6)
	plotFreeSpacePathloss(700e6)
	plotFreeSpacePathloss(4900e6)
	plotFreeSpacePathloss(10000e6)
	plt.show()
