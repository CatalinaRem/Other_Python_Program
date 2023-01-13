code,price = input("Enter product and price: ").split()
price = float(price)
#print(code[0])
if code[0]=="S" or code[0] == "s":
    p = price
    vat = 0
elif code[0]=="T" or code[0] == "t":
    p=price*(100/107)
    vat=price-p

print("Price without tax = %.2f Baht" %p)
print("7%% Tax = %.2f Baht"%vat)