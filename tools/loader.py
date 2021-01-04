import threading, time

class Loader:
	_L = False
	_loader = None
	symbol = "#"
	loader_type = ''

	def __init__(self, symbol = "#", endmsg="Work is done completely....", timespeed=0.1, loader_type='', fnc=lambda:print('Working')):
		self.symbol = symbol
		self.endmsg = endmsg
		self.timespeed = timespeed
		self.fnc = fnc
		self.loader_type = loader_type

	def loadf(self):
		sec = 0
		if self.loader_type == 'time':
			d = 'Time Elapsed: '
			self.fnc(d)
			while not self._L:
				sec += self.timespeed
				self.fnc(f'{d} {sec}seconds')
				time.sleep(self.timespeed)
		else: 
			d = 'Working: '
			self.fnc(d)
			while not self._L:
				d += self.symbol
				self.fnc(d)
				time.sleep(self.timespeed)

		self.fnc(f'\n{self.endmsg}')

	def start(self):
		self._loader = threading.Thread(target=self.loadf)
		self._loader.start()
		return self

	def stop(self):
		self._L = True
		self._loader.join()


if __name__ == "__main__":
	for x in range(2):
		i = Loader().start()
		time.sleep(5)
		i.stop()