from icecream import ic

NR_PSS_LEN = 127  # NR PSS sequence length in frequency domain
NR_PSS_SYMBOL_INDEX = 0  # NR PSS Symbol number
NR_PSS_SUBCARRIER_BEGIN = 56  # NR PSS First Subcarrier index


def NRPSSSequence():
	x_init = [0, 1, 1, 0, 1, 1, 1]
	pass


def getNid(pcid):
	ic(type(pcid))
	if isinstance(pcid, int):
		if pcid < 0 or pcid > 1007:
			nid1, nid2 = -1, -1
			assert False, "pci must be bigger than 0 and less than 1007"
		else:
			nid2 = pcid % 3
			nid1 = pcid // 3
		return nid1, nid2
	else:
		assert False, "pci must be int type"


if __name__ == '__main__':
	pci = 10.1
	Nid1, Nid2 = getNid(pci)
	ic(Nid1, Nid2)
