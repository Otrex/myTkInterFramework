import sys
import os
import manager.snippets as snips

print("--------------------------------------------\n  Note:Use 'Tab' instead of 4 spaces\n------------------------------------------")
args = sys.argv[1:]

commands = {
	"create_view": lambda: createview(*args[1:]),
	"create_model": lambda: createmodel(*args[1:]),
	"start_app": lambda: startapp()
}

def createview(name="Page", *args):
	data = snips.view(name)

	with open("./config/Pages.py", "r") as f:
		cont = f.readlines()

	if name in cont[-5]:
		print("::: View already exists...")
		return
	with open(f"./views/{name}.py", "w") as f:
		f.write(data)

	

	if '#' not in cont[-5]:
		prev = cont[-5].split()
		prev.insert(0, "\t")
		prev.append(",\n")
		cont[-5] = "".join(prev)

	cont.insert(-4, f"\t'{name}': {name}\n")

	# For the import
	cont.insert(2, f"from {name} import {name}\n")

	with open("./config/Pages.py", "w") as f:
		f.writelines(cont)


	print(f":::The View -{name}- has been create.\n:::Go to ./views to edit it...")

def createmodel(name="Dummy", *args):
	data = snips.model(name, *args)

	with open("./config/Models.py", "r") as f:
		cont = f.readlines()

	if name in cont[2]:
		print(":::Model Already Exist...")
		return

	cont.insert(2, f"from models.{name} import {name}\n")

	with open("./config/Models.py", "w") as f:
		f.writelines(cont)

	with open(f"./models/{name}.py", "w") as f:
		f.write(data)

	

	with open("./admin.py", "r") as f:
		cont = f.readlines()

	cont.insert(3, f"\t{name},")
	with open("./admin.py", "w") as f:
		f.writelines(cont)

	print(f":::The Model -{name}- has been created.\n:::Go to ./models to edit")
	print("\n:::Note: The default column type is string, you can change it to any of your choice\nVisit SQLAlchemy documentation for more...")

def startapp(*args):
	os.system("py index.py")

commands[args[0]]()