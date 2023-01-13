integers=[]
integers=input("Enter 13 integers: ").split()
integers2=[]


integers.reverse()
integers2=integers.copy()
integers.reverse()
if integers==integers2:
    print("Symmetric.")
else:
    print("Not symmetric.")