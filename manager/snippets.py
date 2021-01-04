

def view(name) :
	return f"""
#-------------------------------------
#		Page Title : {name}
#-------------------------------------



from core.Page import AbstractPage
from core.Utils import *
# from core.components.tag import *
# from core.components.section import *
# from tkinter import filedialog

class {name}(AbstractPage):
	# use_menu = ''
	def init(self):
		# Place all your StringVar or IntVar variables initialization here
		self.content()

	def content(self):
		# Place your designs here

	# To add menu to your page
	# def menu(self):
	# 	# Your menu
	# 	return menu
	"""



def model(d, *fields):
	c = ""
	r = ""
	f = ""
	for n in fields:
		c += f'{n} = Column(String(100), unique=False)\n\t'
		r += f'{n}=%r '
		f += f', self.{n}'

	return f"""
from core.Database import Base, Column, String, Integer, db_session
from core.Model import AbsModel
# from config.Settings import HASHER

class {d}(Base, AbsModel):
    __tablename__ = '{d}'
    id = Column(Integer, primary_key=True)
    # Use the example bellow to create fields for your DB
    # field_name = Column(String(50), unique=True)
    # note: We have Integer, String etc. Visit SQLAlchemy Docs to learn more
    {c}

    def __repr__(self):
        return '<{d} id=%r {r}>' %(self.id{f})

    # Methods goes here...
"""