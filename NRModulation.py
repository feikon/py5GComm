from cmath import sqrt, pi, exp


def piDiv2BPSK(b_i):
	d_i = exp(1j * pi / 2 * (b_i % 2)) / sqrt(2) * \
            ((1 - 2 * b_i) + (1j - 2j * b_i))
	return d_i


def BPSK(b_i):
	d_i = 1 / sqrt(2) * ((1 - 2 * b_i) + (1j - 2j * b_i))
	return d_i


def QPSK(b_2i0, b_2i1):
	d_i = 1 / sqrt(2) * ((1 - 2 * b_2i0) + (1j - 2j * b_2i1))
	return d_i


def QAM16(b_4i0, b_4i1, b_4i2, b_4i3):
    pass


def QAM64(b_6i0, b_6i1, b_6i2, b_6i3, b_6i4, b_6i5):
    pass


def QAM256(b_8i0, b_8i1, b_8i2, b_8i3, b_8i4, b_8i5, b_8i6, b_8i7):
    pass


if __name__ == '__main__':
	d_00 = QPSK(0, 0)
	d_01 = QPSK(0, 1)
	d_10 = QPSK(1, 0)
	d_11 = QPSK(1, 1)
	print(d_00, '\n', d_01, '\n', d_10, '\n', d_11)
