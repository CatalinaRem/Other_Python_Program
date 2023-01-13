number=input("Enter 10 integers: ").split()
unique_number=[]

for i in range(len(number)):
    if number[i] not in unique_number:
       unique_number.append(number[i])
print(unique_number)

for j in range(0,len(number)):
    k=int(number[j])
    # print(k,end=" ")
