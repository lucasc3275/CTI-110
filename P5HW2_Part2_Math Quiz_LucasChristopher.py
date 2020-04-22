#This program will ask the user for the sum or difference of 2 random numbers and advise if correct or incorrect.
#April 19, 2020
#CTI-110 P5HW2-Part2-Math Quiz
#Christopher Lucas

#Assign global contants add, subtract, & terminate to numbered menu choices
#import random module
#define main function
    #call menu function
    #ask user for desired operation and assign variaable 'selection'
    #if selection == ADD then call user_add function
    #elif selection == SUBTRACT then call user_subtract function
    #elif selection == TERMINATE, display 'the program will now terminate'
    #else display error message and recall main function
#define user_add
    #generate two random numbers and assign seperate variables
    #ask user to add the numbers
    #if user answer does not equal actual answer, display correct answer
    #if user answer answer equals actual answer, congratulate user
    #call main function
#define user_subtract
    #generate two random numbers and assign seperate variables
    #ask user to subtract the numbers
    #if user answer does not equal actual answer, display correct answer
    #if user answer answer equals actual answer, congratulate user
    #call main function


ADD = 1
SUBTRACT = 2
TERMINATE = 3

import random

def main():
    selection = 0
    menu()
    selection = int(input('Please select your desired operation:'))
    if selection == ADD:
        user_add()
    elif selection == SUBTRACT:
        user_subtract()
    elif selection == TERMINATE:
        print('The program will now terminate.')
    else:
        print('ERROR: invalid selection!')
        print('')
        main()
            
def user_add():
    digit_1 = random.randint(1,1000)
    digit_2 = random.randint(1,1000)
    total = (digit_1 + digit_2)
    print('The random numbers are', digit_1, '&', digit_2)
    answer = int(input('Please add the numbers and enter the sum: '))
    if answer == total:
        print('Congratulations, you correctely solved the problem')
    else:
        print('I\'m sorry but the correct answer is', total, '.  Better luck next time!')
    print('')
    main()
        
def user_subtract():
    digit_1 = random.randint(1,1000)
    digit_2 = random.randint(1,1000)
    difference = (digit_1 - digit_2)
    print('The random numbers are', digit_1, '&', digit_2)
    answer = int(input('Please subtract the first number from the second and enter the difference: '))
    if answer == difference:
        print('Congratulations, you correctely solved the problem')
    else:
        print('I\'m sorry but the correct answer is', difference, '.  Better luck next time!')
    print('')
    main()
    
def menu():
    print('------------------Menu------------------')
    print(' 1) Add Random Numbers')
    print(' 2) Subtract Random Numbers')
    print(' 3) Terminate the Program')
    print('----------------------------------------------')

main()