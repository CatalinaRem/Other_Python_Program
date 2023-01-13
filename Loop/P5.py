
debt=float((input("Enter credit card debt: ")))
pay=float(input("Enter monthly payment: "))
i=1
debt=(debt-(pay-(debt*0.015)))
while debt>0:
    print("Month %d : %.2f"%(i,debt))
    debt=(debt-(pay-(debt*0.015)))
    i=i+1
if debt-pay<0:
    print("Month %d : Debt is paid off"%i)
    total=((i-1)*pay)+(debt+pay)
    print("Total payment = %.2f"%(total))
  