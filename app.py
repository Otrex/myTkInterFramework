from core.App import *
from core.SessionHandler import Session



class MyApp(App):
	def init(self):
		self.set_user()
		label = ttk.Label(self, text=self.name.get(), font=LARGE_FONT)
		label.pack(pady=10,padx=10)

	def set_user(self):
		self.name = tk.StringVar()
		self.name.set("WELCOME USER")
		if Session.get():
			self.name.set(Session.get().name.upper())