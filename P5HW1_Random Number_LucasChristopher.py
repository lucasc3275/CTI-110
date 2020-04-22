#This program will generate a random number and challenge the user to guess the number.
#April 11, 2020
#CTI-110 P5HW1-Random Number
#Christopher Lucas

#Display the introduction to the game
#Two functions are used.  The 'main' function executes the game.
#The 'menu' function executes the user controlled menu.
#Define the 'menu' function
    #Display menu
    #instruct user to choose from the menu and assign variable 'selection'
    #if 'selection' equals 1 then call the 'main' function
    #if 'selection' equals 2, the program displays a message and terminates
    #if 'selection' does not equal 1 or 2, the program displays a message and recalls the 'menu' function
#Define the 'main' function
    #import the random function and assign variable 'number' to a random number between 1 and 100.
    #assign 'attempts' variable to keep track of guesses
    #instruct user to enter a number and assign variable 'guess'
    #while 'guess' does not equal 'number' display whether it is too high, too low, or outside the range.
    #if 'guess' equals 'number', congratulate the user and display # of 'attempts'
    #call 'menu' function to restart game
#call the 'menu' function to start game


print(' Care to match wits with a computer? \n This program will randomly generate a number beween 1 and 100. \
\n Your mission, should you choose to accept, is to simply guess that number. \n How good are you? \
 How many times will it take you to guess the number? \n Press 1 to find out, or press 2 and return to your normal boring routine.')

print('')

def main():
    import random
    number=random.randint(1, 100)
    attempts=1
    
    guess=int(input('What is your guess? '))
    
    while guess != number:
        attempts += 1
        if guess < 1 or guess > 100:
            print('We are really starting to question your intellect.  I learned to count in kindergarten, did you?')
            guess=int(input('Lets try this again.  Remember its between 1 and 100: '))
        elif guess > number:
            guess=int(input('Too high, guess again: '))
        elif guess < number:
            guess=int(input('Too low, try again: '))
        
    if guess == number:
        print('')
        print('Great job!!  You may be smarter than we first thought!')
        print('It only took you', attempts, 'times to guess the right number.')
        print('')
        print('Care to try your luck again?')
        print('')
        menu()
        

def menu():
    cstr='or'
    
    print('--------------Main Menu------------ \n   1) Accept the Challenge \n', (cstr.center(40)), \
    ' \n   2) Go Home to Mama \n --------------------------------------------')
    
    selection=int(input('Its time to choose your destiny.  \nWhats it gonna be, 1 or 2?  '))
    
    print('')
    
    if selection == 1:
        main()
    elif selection == 2:
        print('Tell her we said hello!!')
    else:
        print('There was only 2 choices, how did you mess that up?')
        print('')
        menu()

menu()
