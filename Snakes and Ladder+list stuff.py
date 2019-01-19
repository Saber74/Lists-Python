#listexercises.py
##from random import *
##names=['vinh','wahid','cael','maggie','shahed']
##emotions=['loves','likes','hates','hugs','misses']
##a=randint(0,4)
##b=randint(0,4)
##c=randint(0,4)
##print(names[a]+" "+emotions[b]+" "+names[c]) 
##
##print(choice(names)+" "+choice(emotions)+" "+choice(names))
##

#2
##fruits=["apples","bananas","grapes","pears","orange","kiwi"]
##prices=[1.49,0.67,2.39,1.99,1.89,2.79]
##print("-"*40,"\n","Joeseph's fruit market".center(40,"*"),"\n"+"-"*40)
##i=0
##for f in fruits:
##    print(f,"\t\t",(prices[i])
##    i=i+1

#3



t=0
namelist=[]
weedlist=[]
total=0
for i in range (5):
    namelist.append(input("Enter name here:  "))
    weedlist.append(int(input("How many plants they pulled? :  ")))
    b=sum(weedlist)

for i in range(5):
    print("*"*30)
    print(namelist[i],100*weedlist[i]/b)
    print("*"*30)

#4
##from random import *
##p1=0
##p2=0
###starting positions
##turn=1# turn will either be 1 or 2
##ladders=[ 6,24,30,49,82]
##laddersTop=[17,26,44,62,86]
##
##snakes=     [14,20,39,66,69,79,84,88]
##snakesBot=  [ 3,15,33,53,58,67,71,36]
##
##playing=True #boolean variable
##while playing:
##    print("Player",turn,"hit Enter to roll")
##    n=input()  # waiting for him to hit enter
##    if n.lower()=="x":
##        break
##    r=randint(1,6)
##    print("You rolled",r)
##### moving players
##    if turn==1:
##        if p1+r<91:
##            p1=p1+r
##        if p1 in ladders:
##            ind=ladders.index(p1) #ind will be 0,1,2,33 or 4)
##            p1=laddersTop[ind]
##            print("You climbed a ladder")
##        if p1 in snakes:
##            ind=snakes.index(p1) #ind will be 0,1,2,33 or 4)
##            p1=snakesBot[ind]
##            print("You got on a snake psssss")
##        print("You are at spot", p1)
##    if turn==2:
##        if p2+r<91:
##            p2=p2+r
##        if p2 in ladders:
##            ind=ladders.index(p2) #ind will be 0,1,2,33 or 4)
##            p2=laddersTop[ind]
##            print("You climbed a ladder")
##        if p2 in snakes:
##            ind=snakes.index(p2) #ind will be 0,1,2,33 or 4)
##            p2=snakesBot[ind]
##            print("You got on a snake psssss")
##        print("You are at spot",p2)
##
##    if p1==90:
##        print("Player 1 won")
##        break
##    if p2==90:
##        print("Player 2 won")
##        break
##    turn=3-turn
##
##print("done")
##
##
