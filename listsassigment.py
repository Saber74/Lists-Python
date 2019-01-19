#listsassigment exc1

total=0
mark=[] #list for makrs entered by student
while True:
    hisMark=float(input("Enter your marks: \n -1 to stop:")) #allows the user to enter his marks 
    if hisMark==-1:
        break
    mark.append(hisMark) #to add the input to the list
    print(mark)

mark.sort(reverse=True) #sorts from biggest to smallest
total=sum(mark[0:6]) #takes first 6 marks(top) and adds them
avg=total/6 #to find average
print(avg)

'''

#exc2

month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #list of days per month
numOne=int(input("Enter the first number: ")) #to get month
numTwo=int(input("Eneter the second number: ")) #to get day
day=numTwo+sum(month[0:numOne-1]) #to sum all numbers from index 0 to index of the given month number 
print("This is day",day)
'''
#exc3

#knowing that a thing such as memory exists and that making a list = to another is basically linking them to be one as in list1 is list2>> True would have saved time :(
from random import*
from copy import deepcopy as nizar
t=0
counter=0 #for how many times names are inputed
list1=[] #gives gift
while True:
    name=input("x to exit\nEnter your name:   ")
    if name.lower()=="x":
        break
    list1.append(name) #adds name to list
    counter+=1
list2=nizar(list1) #copies list (for recieving gifts)
a=list2.pop() #removes last item and stores it
list2.insert(0,a) #to insert pop value in start to have 2 diffrent lists
print(list1)
print(list2)
while t in range(counter): #while loop to stop when everyone got a gift
    print(list1[t],"is to give",list2[t])
    t+=1 #counter to reach counter to stop
    
    


#ex4
from random import *
counter=0
t=0
randomizer=""
winningCountry=["uruguay","italy","italy","uruguay","germany","brazil","brazil","england","brazil","germany","argentina","italy","argentina","germany","brazil","france","brazil","italy","spain","germany"]
year=["1930","1934","1938","1950","1954","1958","1962","1966","1970","1974","1978","1982","1986","1990","1994","1998","2002","2006","2010","2014"]
percent=[0,12.5,25,37.5,50,62.5,75,87.5,100]
comment=["A zero is never good,try your best to improve","Need to expand your trivia knowledge","A quarter! that's right once every 4 times","less than half, improve your knowledge","That's 1/2 the points,not quite there yet","This is pretty great! above 50 percent","Only 1/4 wrong that's awesome","Too close to perfection","Perfect!!You know too much"]
while t in range(8): #for 8 questions
    randomizer=randint(0,len(year)-1) #for random number
    yearForQuestion=year[randomizer]
    question=input("What country won world cup in %s: "%yearForQuestion)
    t+=1
    ind2=winningCountry[randomizer]
    print("answer is",ind2)
    if question.lower()==ind2:
        counter+=1 #to count correct answers
    del year[randomizer]
    del winningCountry[randomizer]
print("you got",percent[counter],"\n"+comment[counter])     

  


    














































    
