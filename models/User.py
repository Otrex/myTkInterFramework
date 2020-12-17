from core.Database import Base, Column, String, Integer, db_session
from core.Model import AbsModel
from config.Settings import HASHER

class User(Base, AbsModel):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    _password = Column(String(500), default = None, unique=True)

    def __init__(self, name=None, email=None):
    	self.name = name
    	self.email = email

    def set_password(self, password):
    	self._password = HASHER(password.encode()).hexdigest()

    @classmethod
    def auth(cls, email = None, password = None):
    	password = HASHER(password.encode()).hexdigest()
    	user = cls.query.filter(cls.email == email).first()
    	if user:
    		if user._password == password:
    			return user
    		else:
    			return None
    	else:
    		return None 

    def __repr__(self):
        return '<User name="%r" email="%r">' % (self.name, self.email)
