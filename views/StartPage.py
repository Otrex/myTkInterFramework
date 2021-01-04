from core.Page import AbstractPage
from core.Utils import tk, ttk, Session
# from core.components.tag import HorizontalMenu, DropdownMenu
# from core.components.section import flexSection
# from tkinter import filedialog

class StartPage(AbstractPage):
	# use_menu = ''
	def init(self):
		self.info = tk.StringVar()
		self.info.set("Welcome User....")
		self.content()
		self.footer()

	def content(self):
		pass
		# Put content here


	def footer(self):
		pass




