n=int(input("Enter n: "))
for i in range(1,n+1):
    print(i, end=" ")
print("\n-----------------")
for i in range(1,n+1):
    print(i, end=" ")
    if i%10 == 0:
        print()

x = "x"
print("\n-----------------")
for i in range(1,n+1):
    if i%5 == 0:
        print("X",end=" ")
    else:
        print(i,end=" ")
    if i%10 == 0:
        print()
