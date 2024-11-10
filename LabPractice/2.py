from operator import itemgetter
name = []
score = []

while True:
    name_score = input("Enter student name and score: ").split()
    namee = name_score[0]
    scoree = name_score[1]
    if namee == 'end' and scoree =='0':
        break
    else:
        if scoree.isnumeric():
            scoree = int(scoree)

            if namee in name:
                print("Duplicate name!")
            else:
                if 0 <= scoree <= 100:
                    name.append(namee)
                    score.append(scoree)
                else:
                    print("Invalid score!")
        else:
            print("Invalid score!")

def OutPut():
    
        f = sorted(zip(name, score), key=itemgetter(1), reverse=True)
        for n,s in f:
            print("%s\t%s" %(n,s))
    

if name and score:
    print("List: ")
    OutPut()
else:
    print("> empty list!")