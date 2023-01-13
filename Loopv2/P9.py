for st in range(1,4):
    print("Student %d:" %st)
    total = 0
    for sb in range(1,6):
        score=int(input("     Subject %d " %sb))
        total += score
    print("Total score of student %d is %d." %(st,total))