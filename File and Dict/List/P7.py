item=[]
while True:
    item1=input("Item to buy: ")
    if item1 in ['',' ','  ']:
        print("There are",len(item),"items in your shopping list:\n",item)
        if len(item)>5:
            a=0
            for i in range(5,len(item)):
                item.pop()
                a=a+1
            print("Too many items, removing",a,"last items")
            print("Final shopping list:\n",item)
        break
    else:
        item.append(item1)
