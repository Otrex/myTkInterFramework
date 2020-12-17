import tkinter as tk
from tkinter import ttk

class Section(ttk.Frame):
	def __init__(self, parent, **kwargs):
		super().__init__(parent, **kwargs)

class LabeledSection(ttk.LabelFrame):
	def __init__(self, parent, text="", **kwargs):
		super().__init__(parent, text=text,**kwargs)


class Accordian(ttk.Notebook):
	def __init__(self, parent, **kwargs):
		super().__init__(parent, **kwargs)

class flexSection(tk.PanedWindow):
	def __init__(self, parent, **kwargs):
		super().__init__(parent, **kwargs)