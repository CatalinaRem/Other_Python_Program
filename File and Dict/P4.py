name_score={}
for i in range(0,10):
    stu,score=input("Enter name and score: ").split()
    score=float(score)
    name_score[stu] = score

print("--------------------")
print("Sorted student data:")

for i in sorted(name_score.keys()):
    print(i,end=" ")
    print("%.2f"%name_score[i])

score_val=name_score.values()
smax = max(score_val)
smin = min(score_val)

namemax = max(name_score, key=name_score.get)
namemin = min(name_score, key=name_score.get)

print("--------------------")

print("Student(s) with max score of %.2f: %s"%(smax,namemax))
print("Student(s) with min score of %.2f: %s"%(smin,namemin))

print("--------------------")


while True:
    name = input("Enter your query name: ")
    if name in name_score.keys():
        print("Score of",name,"is %.2f"%(name_score[name]))
        if name_score[name] >= 50:
            print(name,"has PASSED the exam.")
        else:
            print(name,"has NOT passed the exam.")
    elif name in ['quit','Quit']:
        print("Bye")
        break
    elif name in ['exit','Exit']:
        print("Bye")
        break
    else:
        print(name,"is not in the database.")


