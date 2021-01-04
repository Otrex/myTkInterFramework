import tkinter as tk
from tkinter import ttk
from config.Settings import *

class AbstractPage(tk.Frame):
    use_menu = ''

    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.params = kwargs;
        self.menu()
        self.init();

    def go_to(self, page):
        self.controller.show_frame(page)
    def menu(self):
    	return tk.Menu(self)


    def init(self, **kwargs):pass
        


