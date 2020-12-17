import tkinter as tk
from tkinter import ttk
from tkinter import Frame, Variable, Scrollbar, Text

from tkinter.constants import VERTICAL, RIGHT, LEFT, BOTH, END, Y

class TextExtension(Frame):
    """Extends Frame.  Intended as a container for a Text field.  Better related data handling
    and has Y scrollbar."""


    def __init__(self, master, textvariable=None, *args, **kwargs):

        super(TextExtension, self).__init__(master)
        # Init GUI

        self._y_scrollbar = Scrollbar(self, orient=VERTICAL)

        self._text_widget = Text(self, yscrollcommand=self._y_scrollbar.set, *args, **kwargs)
        self._text_widget.pack(side=LEFT, fill=BOTH, expand=1)

        self._y_scrollbar.config(command=self._text_widget.yview)
        self._y_scrollbar.pack(side=RIGHT, fill=Y)

        if textvariable is not None:
            if not (isinstance(textvariable, Variable)):
                raise TypeError("tkinter.Variable type expected, " + str(type(textvariable)) + " given.".format(type(textvariable)))
            self._text_variable = textvariable
            self.var_modified()
            self._text_trace = self._text_widget.bind('<<Modified>>', self.text_modified)
            self._var_trace = textvariable.trace("w", self.var_modified)

    def text_modified(self, *args):
            if self._text_variable is not None:
                self._text_variable.trace_vdelete("w", self._var_trace)
                self._text_variable.set(self._text_widget.get(1.0, END))
                self._var_trace = self._text_variable.trace("w", self.var_modified)
                self._text_widget.edit_modified(False)

    def var_modified(self, *args):
        self.set_text(self._text_variable.get())
        self._text_widget.edit_modified(False)

    def unhook(self):
        if self._text_variable is not None:
            self._text_variable.trace_vdelete("w", self._var_trace)
    def clear(self):
        self._text_widget.delete(1.0, END)

    def set_text(self, _value):
        self.clear()
        if (_value is not None):
            self._text_widget.insert(END, _value)
def et(p, **txt):
	return ttk.Label(p, **txt)

def btn(p, **t):
	return ttk.Button(p, **t)

class Input(ttk.Entry):
	def __init__(self, parent, **kwargs):
		super().__init__(parent, **kwargs)

class Textarea(tk.Text):
	def __init__(self, parent, **kwargs):
		super().__init__(parent, **kwargs)

class Show(ttk.Label):
	def __init__(self, parent, **kwargs):
		super().__init__(parent, **kwargs)


class Button(ttk.Button):
	def __init__(self, parent, **kwargs):
		super().__init__(parent, **kwargs)


class Menu(tk.Menu):pass


def HorizontalMenu(parent, menustyle = {}, **menubtn):
	menubar = tk.Menu(parent,**menustyle)
	for label, command in menubtn.items():
		if type(command) == type({}):
			menubar.add_cascade(label=command['label'], menu=command['menu'])

		if type(label) == type({}):
			menubar.add_command(label=label['label'], command=command, **label['style'])

		if type(command) == type({}):continue
		
		menubar.add_command(label=label, command=command)
	return menubar

def DropdownMenu(parent, menuattr={}, mname = None, sep=[], menubtns={}):
	menu = tk.Menu(parent, tearoff=0)
	i = 1
	# if mname:
	for label, command in menubtns.items():
		menu.add_command(label=label, command=command)
		if i in sep:
			menu.add_separator()
		i += 1
	parent.add_cascade(label=mname, menu=menu)

	return menu

