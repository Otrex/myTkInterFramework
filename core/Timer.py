import threading
import time

class Timer(threading.Thread):
	def __init__(self, target = None, time_count = 0, args = []):
		def cover():
			time.sleep(time_count)
			target(*args)
		super().__init__(target = cover)


if __name__ == "__main__":

	def m(g):
		print(f"Kable{g}")

	x = Timer(m, 5, [8])
	x.start()


def setTimeout(self, func, time=0):
	pass