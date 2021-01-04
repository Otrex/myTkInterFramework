from config.Models import *

db = [
	User
]

for dbs in db:
	for i, entries in enumerate(dbs.query.all()):
		print(i+1, ")  " ,entries)

	print("---"*20)

