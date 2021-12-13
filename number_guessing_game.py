# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 15:37:11 2021

@author: dell
"""

import pandas as pd
import random

print("\t\t\tWelcome to number guessing game.")
print("\nHere you have to guess a random number in a given range.")
print("If the difference between the exact number and the guessed number is more than 10, then it will display TOO HIGH or TOO LOW.")
print("Else it will display HIGH or LOW.")
print("-"*20)

liist=[]
e=0
for i in range(4):
    e+=1
    print("Player",e)
    plyname=str(input("Enter the name of player:"))
    print("*"*20)
    liist.append(plyname)
    
ply1=random.choice(liist)
liist.remove(ply1)
ply2=random.choice(liist)
liist.remove(ply2)
ply3=liist[0]
ply4=liist[1]

print("\n\t\t\tFIXTURES")
print("\n\t\t\tMatch 1.)",ply1,"Vs",ply2,"\n\t\t\tMatch 2.)",ply3,"Vs",ply4,"\n\t\t\tMatch 3.) TBD\n\t\t\tFINAL.) TBD")
print("-"*40)
print("\t\t\tMATCH 1\n\t\t\t(",ply1.upper(),"Vs",ply2.upper(),")")
print("-"*40)

win1=None
win2=None
los1=None
los2=None

while True:
    secretnum1=random.randint(1,100)
    secretnum2=random.randint(100,200)
    guessnum1=None
    guessnum2=None
    
    i1=0
    i2=0
    
    print("Get ready",ply1)
    print("-"*25)
    while guessnum1!=secretnum1:
        i1+=1
        guessnum1=int(input("Guess a number between 1 and 100 inclusive:"))
        print("-"*25)
        if guessnum1<secretnum1:
            if secretnum1 - guessnum1>10:
                print("TOO LOW.")
            else:
                print("LOW")
        if guessnum1>secretnum1:
            if guessnum1 - secretnum1>10:
                print("TOO HIGH")
            else:
                print("HIGH")
    print("Correct guess !\nYou took",i1,"attempts.")
    
    print("Now get ready",ply2)
    print("-"*25)
    while guessnum2!=secretnum2:
        i2+=1
        guessnum2=int(input("Guess a number between 100 and 200 inclusive:"))
        print("-"*25)
        if guessnum2<secretnum2:
            if secretnum2 - guessnum2>10:
                print("TOO LOW.")
            else:
                print("LOW")
        if guessnum2>secretnum2:
            if guessnum2 - secretnum2>10:
                print("TOO HIGH")
            else:
                print("HIGH")
    print("Correct guess !\nYou took",i2,"attempts.")
    
    if i1>i2:
        win1=ply2
        los1=ply1
        print("\nCongrats",win1,"! You win and now you are in the FINAL !")
        break
    if i1<i2:
        win1=ply1
        los1=ply2
        print("\nCongrats",win1,"! You win and now you are in the FINAL !")
        break
    if i1==i2:
        print("\nOops ! Its a tie. Both of you have to play again.")
        continue

print("-"*40)
print("\t\t\tMATCH 2\n\t\t\t(",ply3.upper(),"Vs",ply4.upper(),")")
print("-"*40)

while True:
    secretnum3=random.randint(1,100)
    secretnum4=random.randint(100,200)
    guessnum3=None
    guessnum4=None
    
    i3=0
    i4=0
    
    print("Get ready",ply3)
    print("-"*25)
    while guessnum3!=secretnum3:
        i3+=1
        guessnum3=int(input("Guess a number between 1 and 100 inclusive:"))
        print("-"*25)
        if guessnum3<secretnum3:
            if secretnum3 - guessnum3>10:
                print("TOO LOW.")
            else:
                print("LOW")
        if guessnum3>secretnum3:
            if guessnum3 - secretnum3>10:
                print("TOO HIGH")
            else:
                print("HIGH")
    print("Correct guess !\nYou took",i3,"attempts.")
    
    print("Now get ready",ply4)
    print("-"*25)
    while guessnum4!=secretnum4:
        i4+=1
        guessnum4=int(input("Guess a number between 100 and 200 inclusive:"))
        print("-"*25)
        if guessnum4<secretnum4:
            if secretnum4 - guessnum4>10:
                print("TOO LOW.")
            else:
                print("LOW")
        if guessnum4>secretnum4:
            if guessnum4 - secretnum4>10:
                print("TOO HIGH")
            else:
                print("HIGH")
    print("Correct guess !\nYou took",i4,"attempts.")
    
    if i3>i4:
        win2=ply4
        los2=ply3
        print("\nCongrats",win2,"! You win and now you are in the FINAL !")
        break
    if i3<i4:
        win2=ply3
        los2=ply4
        print("\nCongrats",win2,"! You win and now you are in the FINAL !")
        break
    if i3==i4:
        print("\nOops ! Its a tie. Both of you have to play again.")
        continue

dict2={"Fixture":["Match 1","Match 2"],
       "Winner":[win1,win2],
       "Loser":[los1,los2]}
dtf2=pd.DataFrame(dict2,index=[1,2])
print("-"*40)
print("Progress till now -\n")
print(dtf2)
print("-"*40)    
print("\t\t\tREMAINING FIXTURES")
print("\n\t\t\tMatch 3.)",los1,"Vs",los2,"\n\t\t\tFINAL.)",win1,"Vs",win2)
print("*"*50)
print("\t\t\tMATCH 3\n\t\t\t(",los1.upper(),"Vs",los2.upper(),")")
print("-"*50)

win3=None
los3=None

while True:
    secretnum5=random.randint(1,100)
    secretnum6=random.randint(100,200)
    guessnum5=None
    guessnum6=None
    
    i5=0
    i6=0
    
    print("Get ready",los1)
    print("-"*25)
    while guessnum5!=secretnum5:
        i5+=1
        guessnum5=int(input("Guess a number between 1 and 100 inclusive:"))
        print("-"*25)
        if guessnum5<secretnum5:
            if secretnum5 - guessnum5>10:
                print("TOO LOW.")
            else:
                print("LOW")
        if guessnum5>secretnum5:
            if guessnum5 - secretnum5>10:
                print("TOO HIGH")
            else:
                print("HIGH")
    print("Correct guess !\nYou took",i5,"attempts.")
    
    print("Now get ready",los2)
    print("-"*25)
    while guessnum6!=secretnum6:
        i6+=1
        guessnum6=int(input("Guess a number between 100 and 200 inclusive:"))
        print("-"*25)
        if guessnum6<secretnum6:
            if secretnum6 - guessnum6>10:
                print("TOO LOW.")
            else:
                print("LOW")
        if guessnum6>secretnum6:
            if guessnum6 - secretnum6>10:
                print("TOO HIGH")
            else:
                print("HIGH")
    print("Correct guess !\nYou took",i6,"attempts.")
    
    if i5>i6:
        win3=los2
        los3=los1
        print("So",win3.upper(),"you win and you secured 3rd rank.")
        break
    if i5<i6:
        win3=los1
        los3=los2
        print("So",win3.upper(),"you win and you secured 3rd rank")
        break
    if i5==i6:
        print("Oops its a tie. So both of you need to play again !")
        continue
    
print("*"*50)
print("\n\t\t\tTHE FINAL")
print("\n\t\t\t(",win1,"Vs",win2,")")
print("\nHere is a little bit change in the rules.")
print("If the difference between the exact number and guessed number is more than 20, then it will display TOO HIGH or TOO LOW.")
print("Otherwise it will simply display HIGH or LOW.")

win4=None
los4=None

while True:
    secretnum7=random.randint(1,200)
    secretnum8=random.randint(200,400)
    guessnum7=None
    guessnum8=None
    i7=0
    i8=0
    
    print("Get ready",win1)
    print("-"*25)
    while guessnum7!=secretnum7:
        i7+=1
        guessnum7=int(input("Guess a number between 1 and 200 inclusive:"))
        print("-"*25)
        if guessnum7<secretnum7:
            if secretnum7 - guessnum7>20:
                print("TOO LOW.")
            else:
                print("LOW")
        if guessnum7>secretnum7:
            if guessnum7 - secretnum7>20:
                print("TOO HIGH")
            else:
                print("HIGH")
    print("Correct guess !\nYou took",i7,"attempts.")
    
    print("Now get ready",win2)
    print("-"*25)
    while guessnum8!=secretnum8:
        i8+=1
        guessnum8=int(input("Guess a number between 200 and 400 inclusive:"))
        print("-"*25)
        if guessnum8<secretnum8:
            if secretnum8 - guessnum8>20:
                print("TOO LOW.")
            else:
                print("LOW")
        if guessnum8>secretnum8:
            if guessnum8 - secretnum8>20:
                print("TOO HIGH")
            else:
                print("HIGH")
    print("Correct guess !\nYou took",i8,"attempts.")
    
    if i7>i8:
        win4=win2
        los4=win1
        print("So",win4.upper(),"you WIN and you secured 1st position !!")
        break
    if i7<i8:
        win4=win1
        los4=win2
        print("So",win4.upper(),"you win and you secured 1st position !!")
        break
    if i7==i8:
        print("Oops its a tie. So both of you need to play again !")
        continue
    
dict1={"Fixture":["Match 1","Match 2","Match 3","FINAL"],
     "Winner":[win1,win2,win3,win4],
     "Loser":[los1,los2,los3,los4]}

dict3={"Player":[win4,los4,win3,los3],
       "Matches played":[2,2,2,2],
       "Won":[2,1,1,0],
       "Lost":[0,1,1,2]}
dtf3=pd.DataFrame(dict3,index=[1,2,3,4])
dtf1=pd.DataFrame(dict1,index=[1,2,3,4])
print("\n\nSo the overall picture of the tournament is:\n")
print(dtf1)
print("\nAnd the individual performance is:\n")
print(dtf3)
print("\nOnce again congratulations to our winner",win4.upper())
print("\n\t\t\tThanks to all for participating. We hope you enjoyed it.")
        