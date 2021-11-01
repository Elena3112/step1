read="selenium:this is selenium,tkinter:this is kinter"
module={}
a=read.split(",")
for i in a:
	j=i.split(":")
	module[j[0]]=j[1]

print(module.keys())


