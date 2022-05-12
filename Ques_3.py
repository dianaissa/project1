import random
scores=0
print("welcome to network quiz")
name=input("enter your name")
riddle={}
with open("riddles.text",'r')as f:
    questions=f.readlines()
    for question in questions:
        q,a=question.strip().split(':')
        riddle[q]=a
        #print the rules
print("*********RULES*********")
print("maximum question asked=20")
print("correct answer=1 marks")
print("wrong answer=0 marks")

#initialise the questions asked count
qcount=0
#get keys all keys from riddles and convert to list
questions=list(riddle.keys())
#shuffle the list
random.shuffle(questions)
#read each question from the list
for q in questions:
    print(q)
    ans=input("enter your answer")
    #compare both answers by converting to same case and update and print score
    if ans.upper()==riddle[q].upper():
        print("correct answer")
        scores+=1
    else:
        print("better luck next time")
        scores=scores
    print(scores)
    #increment question count and exit if 5 questions asked
    qcount+=1
    if qcount==20:
        break
print("end of quiz")
print(name + " total score= ",scores)
