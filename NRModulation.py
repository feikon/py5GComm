from cmath import sqrt


def BPSK(bt):
    dt = 1/sqrt(2)*((1-2*bt)+(1j-2j*bt))
    return dt


d0 = BPSK(0)
d1 = BPSK(1)
print(d0, '\n', d1)
print(-1/sqrt(2)-1j/sqrt(2))
