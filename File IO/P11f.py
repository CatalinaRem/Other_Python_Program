''' --------------------------
Put your functions here 
------------------------------'''

def rdIncome():
    income=int(input("Enter your income: "))
    return income

def isValid(income1):
    if income1<1000000:
        return income1
    else:
        pass

def compTax(income2):
    if income2<=150000:
        tax=income2*0
        return tax
    elif income2<=500001:
        tax=((income2)*0.1)
        return tax
    elif income2<=1000001:
        tax=((income2-500000)*0.2)+35000
        return tax
    else:
        pass