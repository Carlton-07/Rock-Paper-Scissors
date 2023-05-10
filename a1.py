#Name: Carlton Valerian Gnanamalai
#Topic- Rock-Paper-Scissors game
""" Create a rock,paper,scissors game with the computer in which rock beats scissors, scissors beats paper and paper beats rock. 
    The computer makes a random choice and the user inputs his/her choice and then the game is played.
    The winner is declared and then the user is asked if he/she wants to play again. 
    If the answer is yes, the game is played again but if it is no then it prints a message and the loop ends.
"""

def a1(): 
#defining a function                    
 import random # get access to the random library
 
 while True: # using a while loop to play the game multiple times 
    choices =["rock","paper","scissors"] # declaring a list in a variable named 'choices' 
    
    computer = random.choice(choices)# computer will randomly choose one out of the list of choices
    player = None
    
    while player not in choices:
        player = input("Enter rock,paper or scissors: ").lower() 
        #get input from user and if user inputs capital letters .lower() will change it to lowercase
        
    if player == computer: #if user choice and computer choice are the same
        print("computer: ",computer) #print computers choice
        print("player: ",player) # print user's choice
        print("Tie!") #print the game is a tie
        
    elif player == "rock": # if player chooses rock
        if computer == "paper": # if computer chooses paper
            print("computer: ",computer) #print computers choice
            print("player: ",player) # print user's choice
            print("Computer Wins!") #print computer wins
            print("Better luck next time:)") # print "Better luck next time"
        
        if computer == "scissors": #if computer chooses scissors
            print("computer: ",computer) #print computers choice
            print("player: ",player) # print user's choice
            print("You Win!") #print the user wins
            
    elif player == "paper": # if player chooses paper
        if computer == "scissors": #if computer chooses scissors
            print("computer: ",computer) #print computers choice
            print("player: ",player) # print user's choice
            print("Computer Wins!") #print computer wins
            print("Better luck next time:)") # print "Better luck next time"
        
        if computer == "rock": #if computer chooses rock
            print("computer: ",computer) #print computers choice
            print("player: ",player) # print user's choice
            print("You Win!") #print the user wins
    
    elif player == "scissors": #if player chooses scissors
        if computer == "rock": # if computer chooses rock
            print("computer: ",computer) #print computers choice
            print("player: ",player) # print user's choice
            print("Computer Wins!") #print computer wins
            print("Better luck next time:)") # print "Better luck next time"
        
        if computer == "paper": #if computer chooses paper
            print("computer: ",computer) #print computers choice
            print("player: ",player) # print user's choice
            print("You Win!") #print the user wins

    def repeat(): # defining function   
     play_again = input("\nDo you want to play again?\nyes/no? ").lower()
     #asking user if he/she wants to play again
     
     if play_again == "yes":
        print("\nWelcome back to the game:)")
        a1() #goes back to the start of the game
     elif play_again == "no":#if answer is no 
            print("\nThank you for playing.\nSee you next time:)") # prints "See you next time" 
            exit() # exits the game 
     else : # if user types anything else other than yes or no
        print("\nPlease type yes/no")
        repeat() # goes back to function repeat
        
    repeat()
a1()

   
    

        
            
        
        
            
         
    
    
