w = 3
h = 2*w - 1
print("--- canvas ---")
for r in range(1,h+1):
    for c in range(1,w+1):
        print("*",end=" ")
    print()
def print0(w,h):
    for r in range(1,h+1):
        for c in range(1,w+1):
            if r == 1 or r == h:
                print("*",end=" ")
            elif c == 1 or c == w:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

def print1(w,h):
    for r in range(1,h+1):
        for c in range(1,w+1):
            if c==w:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

def print2(w,h):
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

def print3(w,h):
    for r in range(1,h+1):
        for c in range(1,w+1):
            if r == 1 or r == w or r ==h:
                print("*",end=" ")
            elif c == w:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

def print4(w,h):
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

def print5(w,h):
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

def print6(w,h):
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


def print7(w,h):
    for r in range(1,h+1):
        for c in range(1,w+1):
            if r == 1:
                print("*",end=" ")  
            elif c==w:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

def print8(w,h):
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

def print9(w,h):
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
