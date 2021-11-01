from tkinter import *
root=Tk()
root.attributes("-fullscreen", True)

nameLabel=Label(root, text="Enter your module name")
desLabel=Label(root,text="Enter details")
nameEntry=Entry(root)
desEntry=Entry(root)


def addfn():
	addbtn.pack_forget()
	nameLabel.pack()
	nameEntry.pack()
	desLabel.pack()
	desEntry.pack()
	submitbtn.pack()

def submit():
	file=open("data.txt","a+")
	file.write(nameEntry.get()+":"+desEntry.get()+",")
	file.close()
	
	submitbtn.pack_forget()

	nameLabel.pack_forget()
	nameEntry.pack_forget()
	desLabel.pack_forget()
	desEntry.pack_forget()
	addbtn.pack()



Button(root,text="Exit", command=quit).pack()

addbtn=Button(root, text="add", command=addfn)
submitbtn=Button(root, text="submit",command=submit)
addbtn.pack()


root.mainloop()