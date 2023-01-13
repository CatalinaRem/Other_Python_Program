w = int(input("Enter size: "))
h = 2*w - 1
while True:
    digit = int(input("Enter a digit (0-9): "))
    if digit < 0 or digit > 9:
        print("Bye!")
        break
    if digit == 0:
        for r in range(1,h+1):
            for c in range(1,w+1):
                if r == 1 or r == h:
                    print("*",end=" ")
                elif c == 1 or c == w:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif digit == 1:
        for r in range(1,h+1):
            for c in range(1,w+1):
                if c==w:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif digit == 2:
        for r in range(1,h+1):
            for c in range(1,w+1):
                if r == 1 or r == w or r ==h:
                    print("*",end=" ")
                elif c == w and r <=w :
                    print("*",end=" ")
                elif c == 1 and r >= w:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif digit == 3:
        for r in range(1,h+1):
            for c in range(1,w+1):
                if r == 1 or r == w or r ==h:
                    print("*",end=" ")
                elif c == w:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif digit == 4:
        for r in range(1,h+1):
            for c in range(1,w+1):
                if r == w:
                    print("*",end=" ")  
                elif c==w:
                    print("*",end=" ")
                elif c==1 and r <=w:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif digit == 5:
        for r in range(1,h+1):
            for c in range(1,w+1):
                if r == 1 or r == w or r ==h:
                    print("*",end=" ")
                elif c == 1 and r <=w :
                    print("*",end=" ")
                elif c == w and r >= w:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif digit == 6:
        for r in range(1,h+1):
            for c in range(1,w+1):
                if r == 1 or r ==h:
                    print("*",end=" ")
                elif c==1:
                    print("*",end=" ")
                elif c == 1 and r <=w :
                    print("*",end=" ")
                elif r==w:
                    print("*",end=" ")
                elif c == w and r >= w:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif digit == 7:
        for r in range(1,h+1):
            for c in range(1,w+1):
                if r == 1:
                    print("*",end=" ")  
                elif c==w:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif digit == 8:
        for r in range(1,h+1):
            for c in range(1,w+1):
                if r == 1 or r == h:
                    print("*",end=" ")
                elif c == 1 or c == w:
                    print("*",end=" ")
                elif r == w:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif digit == 9:
        for r in range(1,h+1):
            for c in range(1,w+1):
                if r == 1 or r == w or r == h:
                    print("*",end=" ")  
                elif c==w:
                    print("*",end=" ")
                elif c==1 and r <=w:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    
