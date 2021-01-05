import pickle
import os
from config.Settings import CACHE


class Session:
	@staticmethod
	def register(user):
		with open(CACHE, "wb") as s:
			pickle.dump(user, s)

	@staticmethod
	def get():
		try: 
			with open(CACHE, "rb") as s:
				return pickle.load(s)
		except FileNotFoundError:
			return None

	@staticmethod
	def destroy():
		os.remove("./dep.cache")
