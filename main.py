import time
import re


class Creator:
	message = '{} have created {}'

	def __init__(self):
		self.name = re.sub(r"(\w)([A-Z])", r"\1 \2", type(self).__name__)

	def create(self):
		creation = self.creation()
		time.sleep(1)
		print(self.message.format(self.name, creation.name))
		return creation


class Men(Creator):
	def create_times(self):
		return self.create()


class Times(Creator):
	def create_men(self):
		return self.create()


class StrongMen(Men):
	def __init__(self):
		super().__init__()
		self.creation = GoodTimes


class WeakMen(Men):
	def __init__(self):
		super().__init__()
		self.creation = HardTimes


class GoodTimes(Times):
	def __init__(self):
		super().__init__()
		self.creation = WeakMen


class HardTimes(Times):
	def __init__(self):
		super().__init__()
		self.creation = StrongMen


if __name__ == '__main__':
	men = StrongMen()
	while True:
		times = men.create_times()
		men = times.create_men()
