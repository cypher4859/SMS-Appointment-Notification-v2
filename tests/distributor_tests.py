import pytest


class TestClass:

	@pytest.mark.skip
	@pytest.mark.great
	def test_distribute_to_sender(self):
		pass

	@pytest.mark.skip
	@pytest.mark.great
	def test_distribute_to_scheduler(self):
		pass
