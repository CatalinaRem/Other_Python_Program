number=input("Enter 10 integers: ").split()
unique_number=[]

for i in range(len(number)):
    if number[i] not in unique_number:
        unique_number.append(number[i])
print("Unique numbers:",end=" ")

for j in range(0,len(unique_number)):
    k=int(unique_number[j])
    print(k,end=" ")


