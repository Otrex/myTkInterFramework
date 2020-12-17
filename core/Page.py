import tkinter as tk
from tkinter import ttk
from config.Settings import *

class AbstractPage(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.params = kwargs;
        self.init();


    def init(self, **kwargs):pass
        


