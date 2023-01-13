items = {}

while True:
   order = input('Item: ')
   if len(order) > 0:
       price = float(input('* price: '))
       items[order] = price
   else:
       break

print('You order:')
for k in items.keys():
   print(k, end='; ')

cost = 0
for k in items.keys():
   cost += items[k]

print(items)
print(price)

# print()
# print('It is ', cost, 'baht.')