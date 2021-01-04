from config.Pages import START_PAGE, OTHER_PAGES
from core.Page import AbstractPage
from core.Utils import *
from app import MyApp

def APP_Login():
	app = MyApp()
	app.title('My Small Apps')
	# app.geometry(f'{app.winfo_screenwidth()}x{app.winfo_screenheight()}')
	app.geometry('500x400')
	app.add_frames(
		startpage = START_PAGE,
		otherpages = OTHER_PAGES
	)

	app.mainloop()