k=int(input("Input number of value(s): "))
if k == 1:
    sum=float(input())
    print("Weighted Avg = %.4f"%sum)
else:
    x=input().split()
    item=1
    a=1.0
    for item in x:
        item=float(item)
        a=float(a)
        a=(a+item)/2
    print("Weighted Avg = %.4f"%a)