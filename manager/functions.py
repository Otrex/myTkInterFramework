
import os
def copy(filename, pathto):
	print(os.getcwd())
	nfn = filename.split("/")[-1]
	with open(pathto + nfn, 'w') as k:
		with open(filename, 'r') as f:
			for x in f.read():
				k.write(x)
