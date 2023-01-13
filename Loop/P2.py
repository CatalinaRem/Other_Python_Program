n=int(input("Enter n: "))
a="*"
b="!"
for i in range(1,n+1):
    if i%5 ==1:
        print(b,end="")
    else:
        print(a,end="")