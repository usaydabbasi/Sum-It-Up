#File Name: Sum It Up
#Description: This program rolls three die and clears the rack based off of what die are chosen.
#Test Cases: Rolling die

import random
import time
rackp = [2,3,4,5,6,7,8,9,10,11,12,13,14]
compr = ['-','-','-','-','-','-','-','-','-','-','-','-','-']
playr = ['-','-','-','-','-','-','-','-','-','-','-','-','-']


#__________________________________________________________________________


#rules and instructions to the game
def displayRules():
    name = input("Please enter your name: ")
    print("\n")
    time.sleep(0.5)
    print("Hello",name,"and welcome to Sum It Up!")
    print("\n")
    time.sleep(0.5)
    print("Here are the instructions/rules to this game.")
    print("\n")
    time.sleep(0.5)
    print("a) A rack will be displayed to show you what numbers are left over")
    print("\n")
    time.sleep(0.5)
    print("b) Three seven-sided die will randomly rolled")
    print("\n")
    time.sleep(0.5)
    print("c) The computer or yourself (based on the turn) will choose two numbers that add up to a number on your rack")
    print("\n")
    time.sleep(0.5)
    print("d) If the number is available on your rack, then that number will clear based off your selection")
    print("\n")
    time.sleep(0.5)
    print("This process will repeat until one persons rack is cleared.")
    print("\n")
    time.sleep(0.5)
    print("ENJOY AND HAVE FUN!")
    print("\n")


#display computer rack
def compRack(compr, playr):
    index = 0
    pos = 0
    print("\nComputer Rack:")
    print("      ", end='')
    for x in range (0,13):
        print(str(rackp[x]).ljust(8), end = "")
        pos += 1
    print("")
    print("      ", end='')
    for y in range (0,13):
        print((compr[y]).ljust(8), end = "")
        index += 1

        
#display player rack
def playerRack(compr, playr):
    index = 0
    pos = 0
    print("\n User Rack:")
    print("      ", end='')
    for x in range (0,13):
        print(str(rackp[x]).ljust(8), end = "")
        pos += 1
    print("")
    print("      ", end='')
    for y in range (0,13):
        print((playr[y]).ljust(8), end = "")
        index += 1


#rolls random dice
def dice():
    roll1=random.randint(1,7)
    roll2=random.randint(1,7)
    roll3=random.randint(1,7)
    return roll1,roll2,roll3


#function that adds number
def select(playr):
        x = []
        x.append(roll1)
        x.append(roll2)
        x.append(roll3)
        sum2 = roll1 + roll2
        sum3 = roll1 + roll3
        sum4 = roll2 + roll3
        index1 = sum2 - 2
        index2 = sum3 - 2
        index3 = sum4 - 2
        try:
            if "X" not in playr[index1] or "X" not in playr[index2] or "X" not in playr[index3]:
                select1 = int(input("Please enter the first number out of the dice you would like to add: "))
                while select1 not in x:
                    print("Please select a different number from your rolls!")
                    select1 = int(input("Please enter the first number out of the dice you would like to add: "))
                x.remove(select1)
                select2 = int(input("Please enter the second number out of the dice you would like to add: "))
                while select2 not in x:
                    print("Please select a different number from your rolls!")
                    select2 = int(input("Please enter the second number out of the dice you would like to add: "))
                sum1 = select1 + select2
                while sum1 < 15:
                    if sum1 == sum2 or sum3 or sum4:
                        if sum1 in rackp:
                            index = sum1 - 2
                            del(playr[index])
                            playr.insert(index, 'X')
                            playerRack(compr, playr)
                            break
            else:
                print("Sorry, there are no available options, try again next turn!")
                time.sleep(0.3)
                playerRack(compr, playr)
        except ValueError:
            print("Please enter an integer!")
            select(playr)
        return playr



##def check_num(roll1,roll2,roll3):
##    if select2 and select1 != roll1 or select2 and select1 != roll2 or select2 and select1 != roll3:
##        print("Please choose a number that you rolled")
        







#__________________________________________________________________________


#function that adds bots number
def comp_select(compr):
    select3 = random.randint(1,7)
    select4 = random.randint(1,7)
    select5 = random.randint(1,7)
    print("The computer rolled:",select3,select4,select5)
    sum4 = select3 + select4
    sum5 = select3 + select5
    sum6 = select4 + select5
    index1 = sum4 - 2
    index2 = sum5 - 2
    index3 = sum6 - 2
    if compr[index1] != "X":
        if sum4 in rackp:
            (compr[index1]) = "X"
    elif compr[index2] != "X":
        if sum5 in rackp:
            (compr[index2])="X"
    elif compr[index3] != "X":
        if sum6 in rackp:
            (compr[index3]) = "X"
    elif sum5 or sum4 or sum6 not in rackp:
        print("Computer could not clear any numbers")
    compRack(compr,playr)
    return compr
   

#___________________________________________________________________________           
#Main Program
print("███████╗██╗   ██╗███╗   ███╗    ██╗████████╗    ██╗   ██╗██████╗")
time.sleep(0.2)
print("██╔════╝██║   ██║████╗ ████║    ██║╚══██╔══╝    ██║   ██║██╔══██╗")
time.sleep(0.2)
print("███████╗██║   ██║██╔████╔██║    ██║   ██║       ██║   ██║██████╔╝")
time.sleep(0.2)
print("╚════██║██║   ██║██║╚██╔╝██║    ██║   ██║       ██║   ██║██╔═══╝")
time.sleep(0.2)
print("███████║╚██████╔╝██║ ╚═╝ ██║    ██║   ██║       ╚██████╔╝██║")
time.sleep(0.2)
print("╚══════╝ ╚═════╝ ╚═╝     ╚═╝    ╚═╝   ╚═╝        ╚═════╝ ╚═╝")   
print(" ")
displayRules()
start = input("Press enter to start the game")
print(" ")
if start == "":
    p = playerRack(compr, playr)
    c = compRack(compr, playr)
    while "-" in playr and "-" in compr:
        roll1, roll2, roll3 = dice()
        print(" ")
        print("You Rolled: ",roll1,roll2,roll3)
        print(" ")
        playr = select(playr)
        print("\n")
        time.sleep(1.5)
        compr = comp_select(compr)
        time.sleep(1.5)
        print("\n")
    print("GAME OVER!")


#function that narrows down possible answers
##def posanswers(dice):
##    possanswers = []
##    for x in range(0, len(dice)):
##        for y in range(i + 1, len(dice)):
##            possible = dice[i] + dice[p]
##            if possible not in possanswers:
##                if comp_turn == True:
##                    if possible in compr:
##                        possanswers.append(possible)
##                if user_turn == True:
##                    if possible in playr:
##                        possanswers.append(possible)
##    return possanswers

##def possible():
##    possible = []
##    for x in range(0,len(rackp1)):
##        for y in range(x + 1, len(rackp1)):
##            possibility =
##                if possibility not in possible:
##                    if possible in rackp1 or possible in compp1:
##                        possible.append(possibility)
##                        return possible
##                    

###function that replaces index with completed
##def complete():
##    i = 0
##    while i < (len(inventory)):
##            newName = ("X")
##            del(inventory[i][1])
##            inventory[i].insert(1,newName.title().replace(" ",""))
##            print("\n")
##            return None                    
##        i+=1
##    print("\n")
##   

###player selects dice to add
##def select():
##    select1 = input("Please enter the value of the dice you would like to add to your rack: ")
##    select2 = input("Please enter the value of the dice you would like to add to your rack: ")
##    if select1 and select2 == roll1 and roll2:
##        ...
##    if select1 and select2 == roll1 and roll3:
##        ...
##    if select1 and select2 == roll2 and roll3:
##        ...
##    else:
##        print("Sorry Invalid Entry, Try Again!")
        
    
