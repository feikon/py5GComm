from NRModulation import piDiv2BPSK, BPSK


def test_1_puls_1_equl_2():
    assert 1 + 1 == 2


def test_piDiv2BPSK_give0_return_0():
    assert piDiv2BPSK(0) == 0
