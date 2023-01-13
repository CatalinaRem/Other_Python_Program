do = {}
while True:
    todo=input("To do: ")
    if len(todo) > 0:
        detail = input("* details: ")
        do[todo] = detail
    else:
        break

print("You have %d thing(s) to do:"%len(do))
for i in sorted(do.keys()):
    print("*",i)
command = input("Command (enter name for details or 'all' for everything): ")
if command in ['all','All','aLl','alL','ALl','aLL']:
    for i in sorted(do.keys()):
        print("*",i)
        print("**",do[i])
elif command in do.keys():
    print("*",command)
    print("**",do[command])
else:
    print("Bye")
