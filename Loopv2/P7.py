n=int(input("Enter n: "))
for r in range(1,n+1):
    for c in range(1,n+1):
        if r==n:
            print("*",end=" ")
        elif r+c >= n+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()