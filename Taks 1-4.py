# Databricks notebook source
#Task 1 (Rolling Dice)

import random
roll_dice = "Yes"
while roll_dice:
    if roll_dice == "Yes":
        print("The random rolled  number is :", random.randint(1,6)) #(prints random number between 1-6)
        repeat = (input("Do you want to roll dice again?: Yes or No")) #(procceds to ask user if they want to roll dice again)
    
    if repeat == "Yes": #(if users input matches then proceeds to roll another random number)
        roll_dice = "Yes" 
    else: #(loops till it gets answer yes or no)
        roll_dice = "No"
        print("Thanks for playing")
break #(end of loop)

# COMMAND ----------

#Task 2 (Guess the randomly generated number)
import random
n = random.randint(1,50)                         #(The n is randomly generated to be between 1-50)
guess = int(input("Enter Number between 1-50:")) #(ask user to input(converts it into integern) number between 1-50)
while n!= guess:                                 #(if both aren't equal return true)
    if guess < n:                                #(if the inputed number is less than generated number, then it prints number is too low)
        print("The number is too low")
        guess = int(input("Enter number again")) #(ask user to intput number again)
    elif guess > n:                              #(if user input number above chosen number it will be say its to had and procced to ask for input again)
        print("The number is too high")
        guess = int(input("Enter number again"))
    else:
        break
print("The number you guessed is correct")      #(if user enters connect number it will give out this message)
        

# COMMAND ----------

#Task 3 (Ask user for serious of worded input and them add them to story template)
print("Please answer series  of questions to generate template")#(message in beginning to tell user what to do)
#(Below is series of question, it will ask user to enter, before transfering data onto template)
input1 = input("What is your name?") 
input2 = input("Where are you from")
input3 = input("What company do you work?")
input4 = input("Where is you company based")
#input5 = 
#input6 = 
#input7 = 
#input8 = 
#input9 = 
#input10 =  
#(below is template that will be shown once required data is entered)

print("Hi my name is" ,input1, "and I am from" ,input2, ",I work at" ,input3, "and our company is based at", input4)

# COMMAND ----------

#Task 4 (Adventure Game)

#Introduction
#if __name__ == "__main__":
    #while True:
        #print("Welcome to Adventure Game!")
        #print("As an avid adventurer, on your tracks you've got lost and must find your way out!!")
        #print("You can walk in multiple directions, you can also choose to fight monster or die!!!!!")
        #print()
        #name = input("What's your name adventurer?")
        #print("Good luck",name, "on your adventure and let's see if you can make it out.")
        #print()
        #starting_room()
        

def starting_room():
    directions = ["Down" , "Right"]
    print("Your are in your first room, where shall we go??")
    print("You can choose to go in two directions, Which direction would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("You can either go Down or Right")
        userInput = input()
    if userInput == "Down":
         room3()
    elif userInput == "Right":
         room2()
    else:
        print("Please enter direction based on selection available")

def room2():
    print("You find this door opens into a wall")
    print("You are now back to starting postion")
    starting_room()

def room3():
    direction = ["Left" , "Down" , "Right"]
    print("You've entered into a next room, which direction are we heading now?")
    userInput = ""
    while userInput not in direction:
        print("Your options: Right/Down/Left")
        userInput = input()
        if userInput == "Left":
            print("Sorry this door opened into a wall")
        elif userInput == "Down":
            room4()
        elif userInput == "Right":
            room5()

def room4():
    direction = ["Left" , "Right"]
    print("You've entered into a next room, which direction will you be heading now?")
    userInput = ""
    while UserInput not in direction:
        userInput = input()
        if userInput == "Left":
            print("This door has led you back to starting room")
            starting_room()
        elif userInput == "Right":
            room6()

def room5():
    direction = ["Up", "Down" , "Right"]
    print("Choose where you going next")
    userInput = ""
    while userInput not in direction:
        if userInput == "Up":
            print("Sorry this door opened into a wall")
        elif userInput == "Right":
            print("Sorry this door opened into a wall")
        elif userInput == "Down":
            room6()
    
    

    
    
    
    
    
    
    
    
if __name__ == "__main__":
    while True:
        print("Welcome to Adventure Game!")
        print("As an avid adventurer, on your tracks you've got lost and must find your way out!!")
        print("You can walk in multiple directions, you can also choose to fight monster or die!!!!!")
        print()
        name = input("What's your name adventurer?")
        print("Good luck",name, "on your adventure and let's see if you can make it out.")
        print()
        starting_room()  
    
    
    
    

# COMMAND ----------


def room3():
    direction = ["Left" , "Down" , "Right"]
    print("You've entered into a next room, which direction are we heading now?")
    userInput = ""
    while userInput not in direction:
        print("Your options: Right/Down/Left")
        userInput = input()
        if userInput == "Left":
            print("Sorry this door opened into a wall")
        elif userInput == "Down":
            room4()
        elif userInput == "Right":
            room5()

def room2():
    print("You find this door opens into a wall")
    print("You are now back to starting postion")
    starting_room()


def starting_room():
    directions = ["Down" , "Right"]
    print("Your are in your first room, where shall we go??")
    print("You can choose to go in two directions, Which direction would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("You can either go Down or Right")
        userInput = input()
    if userInput == "Down":
         room3()
    elif userInput == "Right":
         room2()
    else:
        print("Please enter direction based on selection available")


if __name__ == "__main__":
    while True:
        print("Welcome to Adventure Game!")
        print("As an avid adventurer, on your tracks you've got lost and must find your way out!!")
        print("You can walk in multiple directions, you can also choose to fight monster or die!!!!!")
        print()
        name = input("What's your name adventurer?")
        print("Good luck",name, "on your adventure and let's see if you can make it out.")
        print()
        starting_room()
        

# COMMAND ----------


