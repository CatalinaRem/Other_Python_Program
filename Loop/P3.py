while True:
    a,c,b=input("Enter x op y (+ - * / // %): ").split()
    a=float(a)
    b=float(b)
    if a == 0 and b == 0:
            print("Bye!")
            break
    if c=="+":
        d=a+b
        print("%.2f %s %.2f = %.2f" 
        %(a,c,b,d))
    elif c=="-":
        d=a-b
        print("%.2f %s %.2f = %.2f" 
        %(a,c,b,d))
    elif c=="*":
        d=a*b
        print("%.2f %s %.2f = %.2f" 
        %(a,c,b,d))
    elif c=="/":
        if b == 0:
         print("divider is 0")
        else:
            d=a/b
            print("%.2f %s %.2f = %.2f" 
            %(a,c,b,d))
    elif c == "//":
        if b == 0:
            print("divider is 0")
        else:
            d=a//b
            print("%d %s %d = %.d" 
            %(a,c,b,d))
    elif c == "%":
        d=a%b
        print("%d %s %d = %d" 
        %(a,c,b,d))
    elif c=="^":
        d=a**b
        print("%.2f %s %.2f = %.2f" 
        %(a,c,b,d))
    else:
        print("Wrong op.")