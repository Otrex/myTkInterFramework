import os
import glob

def navigate(dir):
	dirs = dir.split('\\')

class Paths:
	__paths = []
	i = 0; x= []
	def __init__(self, basedir = os.getcwd()):
		self._basedir = basedir
		self.getdocs()

	def getdocs(self):
		# Get the list of all files in directory tree at given path
		listOfFiles = list()
		for (dirpath, dirnames, filenames) in os.walk(self._basedir):
			listOfFiles += [os.path.join(dirpath, file) for file in filenames]

		for d in listOfFiles:
			self.__paths.append(self.remove(d, os.getcwd()))

		self.__paths.reverse()

	@property
	def getpaths(self):
		return self.__paths

	def remove(self, com, da, split_by = '\\'):
		com = com.split(split_by)
		da = da.split(split_by)
		return split_by.join([x for x in com if x not in da])

	@property
	def refinepaths(self):
		dic = []
		i = 0
		for p in self.__paths:
			parray = p.split('\\')
			dic.append(self._resolve(parray))
		return dic

	def _resolve(self, d):
		dic = {}
		if len(d) > 2:
			dic[d[0]] = self._resolve(d[1:])

		if len(d) == 2:
			dic[d[0]]  = d[1]

		if len(d) == 1:
			dic[''] = d[0]

		return dic

	def treelize(self):
		dic = {}
		ps = self.refinepaths
		for p in ps:
			for x, y in p.items():
				if type(y) == type ({}):pass
				if x in dic:
					dic[x].append(y)
				else :
					dic[x] = [y]
		return dic


if __name__=='__main__':
	os.chdir('../uploads')
	x = Paths(os.getcwd())
	print(x.getpaths)
	print(x.treelize())

