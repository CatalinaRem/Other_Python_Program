i = 0 #initalization
#while
n = int(input("Enter n:"))
while i < n: #condition
    print(i+1)
    i+=1 #update
print("---------")

#j = int(input("Enter j:"))
#range(n) => 0,1,...,n-1
#range(1,n) => 1,2,...,n-1
#range(1,n+1) => 1,2,...,n
for j in range(n+1):
    print(j)