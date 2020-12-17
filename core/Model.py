from .Database import db_session

class AbsModel:
	__tablename__ = 'abs'
	def __repr__(self):
		return f'<{self.__dir__}>'

	@classmethod
	def filter(cls):
		return db_session.query(cls).filter

	def save(self):
		db_session.add(self)
		db_session.commit()