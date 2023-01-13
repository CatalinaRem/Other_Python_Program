size=int(input("Enter a size: "))
integer=[]
integer=input("Enter %d integers: " %size).split()

for i in range(0,size):
    integer.append

print("In order:")

for i in range(0,size):
    print(integer[i],end=" ")


integer.reverse()
print("\nReverse order:")

for j in range(0,size):
    print(integer[j],end=" ")
