import pytest
from SSB import PSS


def test_nid_give_pcid_0_return_nid1_0_nid2_0():
	assert PSS.getNid(0) == (0, 0)


def test_nid_give_pcid_1007_return_nid1_335_nid2_2():
	assert PSS.getNid(1007) == (335, 2)


def test_nid_give_pcid_negtive_1_return_nid1_negtive_1_nid2_negtive_1():
	assert PSS.getNid(-1) == (-1, -1)


def test_nid_give_pcid_1008_return_nid1_negtive_1_nid2_negtive_1():
	assert PSS.getNid(1008) == (-1, -1)
