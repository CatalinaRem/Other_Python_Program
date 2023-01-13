x=float(input("Enter x: "))
i=1
sum=i
a=i+(1/i)
while sum<=x:
    print("Round %d : sum = %.5f"%(i,sum))
    i = i+1
    sum = sum+(1/i)
if sum>x:
    print("Round %d : sum = %.5f"%(i,sum))