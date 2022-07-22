# TODO:plot constellation diagram
from numpy import real, imag
from NRModulation import QPSK
import matplotlib.pyplot as plt


def complex2Point(complex_value):
    """convert complex value to point

    Parameters
    ----------
    complex_value :
        complex value

    Returns
    -------
    x, y
        real(complex) ,imag(complex)
    """
    x, y = real(complex_value), imag(complex_value)
    return x, y


def plotPoint(point):
    plt.plot(0.7, 0.7, 'r')
    plt.show()


if __name__ == '__main__':
    d_00 = QPSK(0, 0)
    print(d_00)
    point = complex2Point(d_00)
    print(point)
    plotPoint(point)
