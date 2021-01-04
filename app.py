from core.App import *
from core.SessionHandler import Session
from core.components.tag import HorizontalMenu, DropdownMenu


# MyApp = App
class MyApp(App):
	def menu(self):
		f = tk.Frame(self)
		f.pack()
		cont = tk.Menu(f)

		drop = DropdownMenu(
			cont, sep = [1],
			menubtns = {
				'LogOff': lambda: self.go_home(),
				'Open' : lambda: filedialog.askopenfilename(),
				'Save' : lambda:'',
				'Save As' : lambda:''
			}
		) 

		menu = HorizontalMenu(
        	f, 
        	File={'menu': drop, 'label':'Home'}, 
        	Home=lambda: self.show_frame('FirstPage'),
			Novel_Reader=lambda: self.show_frame('NovelReader'),
			Manga_Reader=lambda: self.show_frame('MangaReader'),
        	Quit=self.destroy
		) # Replace None with the imported page

		self.config(menu=menu)
		return menu


		# self.config(menu=menu)
	# def init(self):
	# 	self.set_user()
	# 	label = ttk.Label(self, text=self.name.get(), font=LARGE_FONT)
	# 	label.pack(pady=10,padx=10)

	# def set_user(self):
	# 	self.name = tk.StringVar()
	# 	self.name.set("WELCOME USER\n Go to app.py to adjust this")
	# 	if Session.get():
	# 		self.name.set(Session.get().name.upper())