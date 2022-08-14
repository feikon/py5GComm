from math import log10, pi

LIGHTSPEED = 3e8


def freeSpacePathloss(d, lamda=0.11696):
	Lbf = 20 * log10(4 * pi * d / lamda)
	return round(Lbf, 2)


def getLamda(frequency=2565e6):
	lamda = LIGHTSPEED / frequency
	return round(lamda, 5)
