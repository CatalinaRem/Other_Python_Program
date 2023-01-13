import math
x1,y1,x2,y2 = input("Enter x1, y1, x2, y2: ").split()
x1=float(x1)
y1=float(y1)
x2=float(x2)
y2=float(y2)
a=(x1,y1)
b=(x2,y2)
dist=math.sqrt(((x1-x2)**2)+(((y1-y2)**2)))

p1 = (x1,y1)
p2 = (x2,y2)
dis = 0
for i in range(len(p1)):
    dis += abs(p1[i]-p2[i])

print("Please choose your distance: \n        1 Euclidean distance \n        2 Manhattan distance")
choice = int(input("Your choice: "))
if choice==1:
    print("Euclidean distance = %.5f" % (dist))
elif choice==2:
    print("Manhattan distance = %.5f" % (dis))
else:
    print("Error : invalid syntax. please run program and try again")