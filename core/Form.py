import tkinter as tk
from tkinter import ttk
from .DS import Object

class CharField(tk.Frame):
	label = None
	def __init__(self, parent, **kwarg):
		tk.Frame.__init__(self, parent)
		self._data = tk.StringVar()
		self._tag = ttk.Entry(self, textvariable = self._data)

		if "label" in kwarg:
			self.label = ttk.Label(self, text = kwarg["label"])

		if "password" in kwarg and kwarg['password']:
			self._tag["show"] = "*"

		if "lwidth" in kwarg:
			self.label['width'] = kwarg["lwidth"]

	def style_label(self, style = {}):
		for s in style:
			self.label[s] = style[s]

		return self

	def get_data(self):
		return self._data.get()

	def clear(self):
		self._data.set("")

	def style_input(self, style):
		for s in style:
			self._tag[s] = style[s]

		return self

	def place(self, _type="pack", **kwargs):
		if self.label:
			self.label.grid(row=0)
			self._tag.grid(row=0, column=1)
		else :
			self._tag.pack(**kwargs)

		# Self placing
		if _type.upper() == "GRID":
			self.grid(**kwargs)
		if _type.upper() == "PACK":
			self.pack(**kwargs)

		return self



class Form:
	fields = Object()
	def initialize(self, fields={}):
		for f in fields:
			self.form[f].set_data(fields[f])

	@staticmethod
	def set_fields(**kwargs):
		x = Form()
		x.fields = Object()
		for i in kwargs:
			assert isinstance(kwargs[i], tk.Frame)
			x.fields[i] = kwargs[i]

		return x

	def clear_fields(self):
		for f in self.fields:
			f.clear()

	def get_clean_data(self):
		obj = Object()
		for f in self.fields:
			obj[f] = self.fields[f].get_data()

		return obj

	@property
	def cleaned_data(self):
		return self.get_clean_data()
	

