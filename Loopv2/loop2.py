a=9
if a>0:
    print("xx")
else:
    print("Nope")
while a>0:
    print(a,":xx")
    a -= 1
print("-----")
print(range(9))
for i in range(9):
    print(i,": xx")

for d in range(1,11): #ลูปนอก
    for r in range(1,6): #ลูปใน
        print(d,r,"x")
    print()

for d in range(1,11): #ลูปนอก
    for r in range(1,6): #ลูปใน
        print("x",end=" ")
    print()

for d in range(1,11): #ลูปนอก
    for r in range(1,6): #ลูปใน
        print("x", end="-")
    print()
