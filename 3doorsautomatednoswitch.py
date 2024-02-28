#3 doors conundrum
#Is it better odds to switch doors?
#In a quiz show, the contestant has to pick between 3 doors A, B and C.
#Only one door has the prize. The other two have nothing behind them.
#The contestant is asked to choose one.
#Next, the host reveals one of the other doors to be empty.
#He then asks the contestant if they want to switch from their
#original choice to the other door which has not yet been eliminated.
#Is it better odds for the contestant to switch to the other door
#or keep to the original choice?
#The following test will keep the choice to the original choice
#to see what the result is.

import random
rightanswer=""
score=0
eliminate=""
def correctanswer():
    
    ca=random.randrange(1,4)
    #print(ca)
    rightanswer=""
    if ca==1:
        rightanswer="A"
    if ca==2:
        rightanswer="B"
    if ca==3:
        rightanswer="C"
    
    
    randchoice=random.randrange(1,4)
    if randchoice==1:
        choice="A"
    if randchoice==2:
        choice="B"
    if randchoice==3:
        choice="C"
    


    print("computer has chosen", choice)
    global eliminate
    
    if choice=="A" and rightanswer=="B":
        eliminate="C"
    if choice=="B" and rightanswer=="A":
        eliminate="C"
    if choice=="B" and rightanswer=="C":
        eliminate="A"
    if choice=="C" and rightanswer=="B":
        eliminate="A"
    if choice=="C" and rightanswer=="A":
        eliminate="B"
    if choice=="A" and rightanswer=="C":
        eliminate="B"
    if choice=="A" and rightanswer=="A":
        x=random.randrange(1,3)
        if x==1:
            eliminate="B"
        else:
            eliminate="C"
    if choice=="B" and rightanswer=="B":
        x=random.randrange(1,3)
        if x==1:
            eliminate="A"
        else:
            eliminate="C"

    if choice=="C" and rightanswer=="C":
        x=random.randrange(1,3)
        if x==1:
            eliminate="A"
        else:
            eliminate="B"
    
    print("I've got news for you. We can eliminate",eliminate)
    
    #q=input("Do you want to change your mind (y/n)")
    q="n"
    global score
   
    
    if choice==rightanswer:
        if q!= "y":
            score+=1
        print("The choice is correct!")
        print("The score is now", score)
    else:
        print("Computer chose",choice, "That was the wrong answer.")

for n in range(1,10001):

    correctanswer()
print("The score is",score,"out of 10000 attempts.")
  
