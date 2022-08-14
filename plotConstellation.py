from numpy import real, imag
from NRModulation import QPSK
import matplotlib.pyplot as plt


def plotPoint(complex_value):
	x = real(complex_value)
	y = imag(complex_value)
	plt.plot(x, y, 'b*')


if __name__ == '__main__':
	d_00 = QPSK(0, 0)
	d_01 = QPSK(0, 1)
	d_10 = QPSK(1, 0)
	d_11 = QPSK(1, 1)
	plotPoint(d_00)
	plotPoint(d_01)
	plotPoint(d_10)
	plotPoint(d_11)
	plt.show()
