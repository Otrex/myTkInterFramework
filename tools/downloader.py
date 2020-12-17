import requests
import threading

class Download:
	download_path = ""
	def __init__(self, file_path, download_path = ""):
		self.download_path = download_path
		self.file_path = file_path
		self.file_name = file_path.split("/")[-1]
		self.args = []

		
	def start(self):
		self._d = threading.Thread(target = self._start)
		self._d.start()

	def _start(self):
		i = 0
		r = requests.get(self.file_path)
		self._r = r.content
		with open(self.download_path + '' + self.file_name, "wb") as f:
			i += .001
			print(i)
			f.write(self._r)

		if hasattr(self, "on_complete") :
			self._on_complete_callback(self.on_complete, *self.args)

	def _on_complete_callback(self, fnc, *args):
		try:
			return fnc(*args)
		except TypeError:
			print(TypeError)
			raise Exception("Your callback <on_complete>: The args of it are not complete(sha there is an error there...) ")


if __name__ == "__main__":
	import os

	def play(x):
		print(f"{x} is downloaded Successfully....")

	print(os.getcwd())
	x = Download("https://cdn.pixabay.com/photo/2018/09/30/16/26/sun-3713835_960_720.jpg")
	x.on_complete = play
	# x.args = [x.file_name]
	x.start()
