''' --------------------------
Put your functions here 
------------------------------'''

def readInput():
    n1,n2,n3=input("Enter 3 numbers: ").split()
    n1=float(n1)
    n2=float(n2)
    n3=float(n3)
    return n1,n2,n3


def sort(n1,n2,n3):
    number=[]
    number.append(n1)
    number.append(n2)
    number.append(n3)
    number.sort()
    print(number[0],"<=",number[1],"<=",number[2])
