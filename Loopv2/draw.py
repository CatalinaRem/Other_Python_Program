#fff
n = 5
for r in range(1,n+1):
    for c in range(1,n+1):
        if r ==1 or r ==n:
            print("*",end=" ")
        elif c==1 or c == n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#cross
n = 5
for r in range(1,n+1):
    for c in range(1,n+1):
        if r==c:
            print("*",end=" ")
        elif r+c == n+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#plus
n = 5
for r in range(1,n+1):
    for c in range(1,n+1):
        if r==(n+1)/2:
            print("*",end=" ")
        elif c == (n+1)/2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

n = 5
for r in range(1,n+1):
    for c in range(1,n+1):
        if r==(n+1)/2:
            print("*",end=" ")
        elif c == (n+1)/2:
            print("*",end=" ")
        elif r==c:
            print("*",end=" ")
        elif r+c==n+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
