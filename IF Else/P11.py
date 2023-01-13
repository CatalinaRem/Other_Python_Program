a,c,b=input("Enter x op y (+ - * / ^): ").split()
a=float(a)
b=float(b)
if c=="+":
    d=a+b
    print("%.4f" %d)
elif c=="-":
    d=a-b
    print("%.4f" %d)
elif c=="*":
    d=a*b
    print("%.4f" %d)
elif c=="/":
    d=a/b
    print("%.4f" %d)
elif c=="^":
    d=a**b
    print("%.4f" %d)
else:
    print("Invalid op")