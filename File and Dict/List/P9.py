item=int(input("Number of items in a list: "))
integer = []
integer = input("Enter %d integers for the list: "%item).split()
x = int(input("Enter x: "))
insert_at = int(input("Insert at "))

integer.insert(insert_at,x)

print("Final list:",end=" ")
for i in range(0,len(integer)):
    j=int(integer[i])
    print(j,end=" ")

