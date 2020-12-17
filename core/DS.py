
class _Obj:
	@property
	def __dic(self):
		ds = [ x for x in dir(self) if "_" not in x ]
		dic = {i : getattr(self,  i) for i in ds }
		return dic


	def __len__(self):
		ds = [ x for x in dir(self) if "_" not in x ]
		return len(ds)

	def __getitem__(self, i):
		return getattr(self,  i)

	def _values(self):
		return self.__dic.values()

	def __bool__(self):
		return len(self)

	def __setitem__(self, i, a):
		return setattr(self,  i, a)

	def __add__(self, others):
		ds = [ x for x in dir(self) if "_" not in x ]
		ds2 = [ x for x in dir(others) if "_" not in x ]
		dic = {i : getattr(self,  i) for i in ds }
		dic.update({i : getattr(others,  i) for i in ds2 })
		return Object(**dic)

	def __sub__(self, others):
		ds = [ x for x in dir(self) if "_" not in x ]
		ds2 = [ x for x in dir(others) if "_" not in x ]

		for n, i in enumerate(ds):
			if i in ds2:
				if ds[n] == ds2[n]:
					del ds[n]
					del ds2[n]

		dic = {i : getattr(self,  i) for i in ds }
		dic.update({i : getattr(others,  i) for i in ds2 })
		return Object(**dic)

	def __contains__(self, v):
		pass

	def __iter__(self):
		return _ObjIterator(self.__dic)

	def _dict(self):
		return self.__dic


	def __repr__(self):
		d = ''
		ds = [ x for x in dir(self) if "_" not in x ]
		for x in ds:
			d += f' {x}: {getattr(self, x)} '

		return f'<{self.__class__.__name__} {d}>'


class _ObjIterator:
	def __init__(self, items):
		self._items = list(items)
		self._cur = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self._cur < len(self._items):
			item = self._items[self._cur]
			self._cur += 1
			return item
		else:
			raise StopIteration

def Object(**kwargs):
	obj = _Obj()
	for i in kwargs:
		setattr(obj, i, kwargs[i])

	return obj
