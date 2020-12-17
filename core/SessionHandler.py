import pickle
import os


class Session:
	@staticmethod
	def register(user):
		with open('.cache', "wb") as s:
			pickle.dump(user, s)

	@staticmethod
	def get():
		try: 
			with open(".cache", "rb") as s:
				return pickle.load(s)
		except FileNotFoundError:
			return None

	@staticmethod
	def destroy():
		os.remove(".cache")
