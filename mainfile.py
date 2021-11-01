module= {"selenium":"this is a selenium","tkinter":"this is tkinter"}
fns_of_selenium=["function1","function2","function3"]
fns_of_tkinter=["fn1","fn2","fn3"]
fn_dict={"selenium":fns_of_selenium,"tkinter":fns_of_tkinter}
print(module.keys())
a=input("which one you want to see: ")
print(module[a])

print("List of Function")
print(fn_dict[a])
