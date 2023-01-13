psum = 0
pcount = 0
nsum = 0
ncount = 0
while True:
    n = float(input("Enter a number (0 to quit): "))
    if n == 0:
        break
    if n > 0:
        psum += n
        pcount += 1
    else:
        nsum += n
        ncount += 1
#ended loop
if pcount == 0:
    pavg = 0
else:
    pavg = psum/pcount
print("Pos: sum = %.2f Avg = %.2f"%(psum,pavg))
if ncount == 0:
    navg = 0
else:
    navg = nsum/ncount
print("Neg: sum = %.2f Avg = %.2f"%(nsum,navg))