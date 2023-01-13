# v1=[1.0,2.0,3.0,5.0]
# v2=[-1.0,0.0,2.0,2.5]
# vl=4
v1=[]
v2=[]
v3=[]
vl=int(input("Please enter a vector length (n): "))
v1=input("Enter values of the vector v1: ").split()
v2=input("Enter values of the vector v2: ").split()

for i in range(1,vl):
    v1.append
    v2.append

x2=0
print("v1: [",end="")
for i in range(0,len(v1)-1):
    k=float(v1[i])
    print("%.1f"%k,end=", ")
print("%.1f]"%float(v1[i+1]))

print("v2: [",end="")
for i in range(0,len(v2)-1):
    k=float(v2[i])
    print("%.1f"%k,end=", ")
print("%.1f]"%float(v2[i+1]))

for j in range(0,vl):
    x1=float(v1[j])*float(v2[j])
    x2=x2+x1

print("inner product = %.4f"%x2)

    
