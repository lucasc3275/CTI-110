#CTI-110
#P4HW2-Basic Math
#Christopher Lucas
#March 22, 2020

#Assign "selection" variable to control loop
#while selection != 4
    #Display menu options
    #Obtain 2 integer inputs from user and assign variables "digit_1 & digit_2"
    #Add both digits and assign variable "sum"
    #Multiply both digits and assign variable "product"
    #Subtract "digit_1" from "digit_2" and assign variable "difference"
    #User inputs desired operation with assigned variable "selection"
    #While "selection" is < 1 or  > 4, display Error message
    #Prompt the user to reenter a selection from the menu
    #If selection == 1 display the equation and the "sum"
    #Elif selection == 2 display the equation and the "product"
    #Elif selection == 3 display the equation and the "difference"
    #Elif selection == 4 diplay "The program will now terminate"


print('When prompted, please provide two numbers and then choose desired operation from the menu')

print('')

selection='none'

while selection != 4:

    print('------MENU------\n 1)Add Numbers\n 2)Multiply Numbers\n 3)Subtract Numbers \
    \n 4)Exit\n----------------')

    print('')

    digit_1=int(input('Please enter first number:'))
    digit_2=int(input('Please enter second number:'))
    sum=(format(digit_1+digit_2, ',d'))
    product=(format(digit_1*digit_2, ',d'))
    difference=(format(digit_1-digit_2, ',d'))


    selection=int(input('Please select desired operation from the menu:'))

    while selection < 1 or selection > 4:
        print('ERROR: You must select an operation from the menu')
        selection=int(input('Please select operation 1, 2, 3, or 4 from the menu:'))
    
    print('')

    if selection==1:
        print('Your selected operation was', digit_1 ,'+', digit_2)
        print('The answer is:', sum)
    elif selection==2:
        print('Your selected operation was', digit_1 ,'*', digit_2)
        print('The answer is:', product)
    elif selection==3:
        print('Your selected operation was', digit_1 ,'-', digit_2)
        print ('The answer is:', difference)
    elif selection==4:
        print ('The program will now terminate.')

    print('')

