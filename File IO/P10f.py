''' --------------------------
Put your functions here 
------------------------------'''

def read():
    i=0
    number=[]
    while i in range(4):
        a=float(input("Please enter a positive integer: "))
        if a>0:
            number.append(a)
            i=i+1
        else:
            print("Invalid input value. Please try again.")
    return number

def findPower(number):
    import math
    a=number[0]
    b=number[1]
    c=number[2]
    d=number[3]
    z=math.sqrt(((a**b)+(b**c)+(c**d))/10.25)
    print("Z = %.5f"%z)
    return number