#This program will request the user to input a number of feet and convert it to inches.
#April 10, 2020
#CTI-110 P5T2_Feet to Inches
#Christopher Lucas

#Assign 12 to constant of INCHES_PER_FOOT
#Main function obtains user input and assigns variable feet
#Displays feet to inches using feet_to_inches function with the variable 'feet' as an argument.
#feet_to_inches function uses 'feet' as an argument and returns the argument multiplied by INCHES_PER_FOOT (12)
#Call the main function

INCHES_PER_FOOT=12

def main():
    feet=int(input('Enter the number of feet to be converted:'))
    print (feet, 'equals', format(feet_to_inches(feet), ',d'), 'inches.')
             
def feet_to_inches(feet):
             return feet * INCHES_PER_FOOT

main()