from PathLossModel.PathLoss import freeSpacePathloss, getLamda


class TestFreeSpacePathLoss:
	def test_getLamda_frequency_2565MHz_return_0(self):
		assert getLamda(2565e6) == 0.11696

	def test_1_return_40Point62(self):
		assert freeSpacePathloss(1) == 40.62

	def test_0Point1_return_40Point62(self):
		assert freeSpacePathloss(0.1) == 20.62

	def test_0Point01_return_40Point62(self):
		assert freeSpacePathloss(0.01) == 0.62

	def test_100_return_40Point62(self):
		assert freeSpacePathloss(100) == 80.62
