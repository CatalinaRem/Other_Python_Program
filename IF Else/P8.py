income=float(input("Net Income: "))
if income<0:
    print("Wrong input: negative income.")
else:
    pass
if income<=150000:
    tax=income*0
    print("Tax = %.2f Baht" %tax)
elif income<=300000:
    tax=(income-150000)*0.05
    print("Tax = %.2f Baht" %tax)
elif income<=500000:
    tax=((income-300000)*0.1)+7500
    print("Tax = %.2f Baht" %tax)
elif income<=750000:
    tax=((income-500000)*0.15)+27500
    print("Tax = %.2f Baht" %tax)
elif income<=1000000:
    tax=((income-750000)*0.2)+65000
    print("Tax = %.2f Baht" %tax)
elif income<=2000000:
    tax=((income-1000000)*0.25)+115000
    print("Tax = %.2f Baht" %tax)
elif income<=5000000:
    tax=((income-2000000)*0.3)+365000
    print("Tax = %.2f Baht" %tax)
else:
    tax=((income-5000000)*0.35)+1265000
    print("Tax = %.2f Baht" %tax)