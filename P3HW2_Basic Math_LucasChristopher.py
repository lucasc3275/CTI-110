#CTI-110
#P3HW2-Basic Math
#Christopher Lucas
#March 5, 2020

#Obtain 2 integer inputs from user and assign variables "int_1 & int_2"
#Display menu options
#User inputs desired operation with assigned variable "selection"
#If selection == 1 then add the integers & diplay the sum
#Elif selection == 2 then multiply the integers & display the product
#Elif selection == 3 then subtract the integers & display the difference
#Elif selection == 4 diplay "The program will now terminate"
#Else display "Incorrect choice was entered"

int_1=int(input('Please enter first number:'))
int_2=int(input('Please enter second number:'))

print('')

print('------MENU------\n 1)Add Numbers\n 2)Multiply Numbers\n 3)Subtract Numbers \
\n 4)Exit\n----------------')

selection=int(input('Please select desired operation from the menu:'))

print('')

if selection==1:
    print(int_1+int_2)
elif selection==2:
    print(int_1*int_2)
elif selection==3:
    print (int_1-int_2)
elif selection==4:
    print ('The program will now terminate.')
else:
    print ('Incorrect choice was entered.')


