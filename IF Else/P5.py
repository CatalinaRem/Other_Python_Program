hrs = float(input("How many hours do you submit late? "))
print("")
raw = float(input("What is your estimated score? "))

if hrs==0:
    print("Your expected score is %.1f" %raw)
elif hrs<=24:
    score=raw*0.8
    print("Your expected score is %.1f" %score)
elif hrs<=48:
    score=raw*0.5
    print("Your expected score is %.1f" %score)
else:
    print("Your expected score is 0")