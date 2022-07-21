from cmath import sqrt, pi, exp


def piDiv2BPSK(b_i):
	d_i = exp(1j * pi / 2 * (b_i % 2)) / sqrt(2) * \
            ((1 - 2 * b_i) + (1j - 2j * b_i))
	return d_i


def BPSK(b_i):
	d_i = 1 / sqrt(2) * ((1 - 2 * b_i) + (1j - 2j * b_i))
	return d_i


d_0 = piDiv2BPSK(0)
d_1 = piDiv2BPSK(1)
print(d_0, '\n', d_1)
