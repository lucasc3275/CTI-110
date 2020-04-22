#This program will ask the user for the sum of 2 random numbers and advise if correct or incorrect.
#April 19, 2020
#CTI-110 P5HW2-Part1-Math Quiz
#Christopher Lucas

#Define main function
    #Generate 2 numbers and assign variables to each
    #add the 2 numbers and assign variable 'total'
    #display the numbers and  ask user to input the sum of the 2
    #if 'guess' is equal to 'total' diplay congratulatory message
    #else display the correct answer.

import random

print('This program is going to display two random numbers, your job is to add \
those numbers and provide the correct answer')
print('')

def main():
    digit_1=random.randint (1, 1000)
    digit_2=random.randint (1, 1000)
    total=(digit_1 + digit_2)
    print('The two numbers are', digit_1, '&', digit_2)
    guess = int(input('What is the sum of the two numbers? '))
    if guess==total:
        print('Congratulations, you correctely solved the problem')
    else:
        print('I\'m sorry but the correct answer is', total, '.  Better luck next time!')

main()