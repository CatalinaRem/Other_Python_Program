import math
a,b,c=input("Enter coefficients a, b, c: ").split()
# list(map(func,var))
a = float(a)
b = float(b)
c = float(c)
x = b*b - 4*a*c 
if a == 0:
    print("This equation is not quadratic.")
elif x < 0:
    print("This equation has complex roots.")
else: # a !=0 for sure and b**2 -4*a*c >= 0
    root1 = (-b + math.sqrt(x)) / (2*a)
    root2 = (-b - math.sqrt(x)) / (2*a)
    print("The 1st root = %.2f" %root1)
    print("The 2nd root = %.2f" %root2)