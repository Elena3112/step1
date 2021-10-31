module={"selenium":"this is a selenium","tkinter":"this is tkinter"}
def addfn():
	x=input("type the module name: ")
	y=input("type the detail of that module: ")
	module[x]=y


addfn()

print(module)