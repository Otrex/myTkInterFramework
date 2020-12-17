from core.Page import AbstractPage
from core.Utils import tk, ttk, Session
from core.components.tag import HorizontalMenu, DropdownMenu
from core.components.section import flexSection
from tkinter import filedialog

class FirstPage(AbstractPage):
	def init(self):
		self.menusetup()
		self.layout()
		self.rightside()

	def menusetup(self):
		cont = tk.Menu(self.controller)

		drop = DropdownMenu(
			cont, sep = [1],
			menubtns = {
				'Display': lambda: self.controller.go_home(),
				'Open' : lambda: filedialog.askopenfilename(),
				'Save' : lambda:'',
				'Save As' : lambda:''
			}
		) 

		menu = HorizontalMenu(
        	self.controller, 
        	File={'menu': drop, 'label':'Home'}, 
        	Quit=self.close
		) # Replace None with the imported page

		self.controller.config(menu=menu)

	def layout(self):
		self.board = flexSection(self)
		self.board.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
		self.sides()

	def sides(self):
		self.left = flexSection(self.board, bg='grey', orient=tk.HORIZONTAL, width=self.controller.width_by_percent(20))
		self.board.add(self.left)

		self.right = flexSection(self.board, bg='green', orient=tk.HORIZONTAL)
		self.board.add(self.right)

	def rightside(self):
		style = ttk.Style()
		style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
		style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
		style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

		# Set the treeview
		tree = ttk.Treeview(self.right, style="mystyle.Treeview", columns=('Name', 'ID'))
		tree.pack(expand=1,fill=tk.BOTH)
	
		tree.insert('', 'end', 'widgets', text='Widgets')
		tree.insert('', 0, 'apps', text='Applications')

		tree['columns'] = ('size', 'modified')
		tree.column('size', width=50, anchor='center')
		tree.heading('size', text='Size')
		tree.heading('modified', text='Modified')

		tree.set('widgets', 'size', '12KB')
		tree.set('widgets', 'modified', 'Last week')

		tree.insert('', 'end', text='Canvas', values=('25KB Today'))
		tree.insert('apps', 'end', text='Browser', values=('115KB Yesterday'))

		tree.tag_configure('odd', background='#E8E8E8')
		tree.tag_configure('even', background='#DFDFDF')



	def close(self):
		try :
			Session.destroy()
		except:
			print('No Session is stored')
		finally :
			self.controller.destroy()

class LoginView(AbstractPage):
	def __init__(self, parent, controller):
		super().__init__(parent, controller)
		self.controller = controller

		# Error Msg Display
		self.msg = tk.StringVar()
		self.msg.set("")
		errorInf = tk.Label(self, textvariable=self.msg, fg="red")
		errorInf.pack()

		self.form = Form.set_fields(
			email = CharField(self, label = "Email: ", lwidth=15).place(padx=10, pady=5),
			password = CharField(self, label = "Password: ", password=True, lwidth=15).place(padx=10)
		)

		button1 = ttk.Button(self, text="Submit",
                command=lambda: self.auth(**self.form.cleaned_data._dict())).pack(padx=30, pady=10)

	def auth(self, email, password):
		usr = User.auth(email = email, password = password)
		
		if usr:
			Session.register(usr)
			self.controller.destroy()
		else :
			self.msg.set("....Login Failed....")
			t = Timer(target = self.msg.set, time_count = 5, args = [""])
			t.start()
