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
    print(i)
    print("*",do[i])
