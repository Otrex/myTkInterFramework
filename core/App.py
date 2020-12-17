import tkinter as tk
from tkinter import ttk
from config.Settings import *


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.headers()
        self.init()
        

    def headers (self):
        self.tk.call('wm', 'iconphoto', self._w, tk.PhotoImage(file=LOGO))
        self.attributes("-fullscreen", False)
        self.bindings()
        # tk.Tk.iconbitmap(self, default=LOGO)
        tk.Tk.wm_title(self, TITLE)
    
    def init(self):pass

    def bindings(self):
        self.bind("<F11>", lambda e : self.attributes("-fullscreen", True))
        self.bind("<Escape>", lambda e : self.attributes("-fullscreen", False))
        self.add_binding()

    def add_binding(self):pass

    def width_by_percent(self, per):
        return self.winfo_screenwidth() * (per/100)

    def height_by_percent(self, per):
        return self.winfo_screenheight() * (per/100)

    def setup(self):
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand = True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
    def menusetup(self):pass
    def go_home(self):
        self.show_frame('startpage')

    def show_frame(self, cont):
        frame = self.frames[cont]
        print(frame)
        frame.tkraise()

    def add_frames(self, startpage=None, otherpages = [], *frames):
        # Adds the frames to the page
        self.setup()
        self.startpage = startpage
        # otherpages = [] + [{x:c} for x,c in otherpages.items()]
        otherpages.update({'startpage':startpage})
        for name, F in otherpages.items():
            frame = F(self.container, self)
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame('startpage')