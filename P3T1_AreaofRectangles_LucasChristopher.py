#This program will test the area of two rectangles based on user input and tell which one is larger.
#March 3, 2020
#CTI-110 P3T1 Area of Rectangles
#Christopher Lucas



#Have user input the length and width of rectangle A
Length_A = int(input('Enter the length of rectangle A:'))
Width_A = int(input('Enter the width for rectangle A:'))

#Have user input the length and width of rectangle B
Length_B = int(input('Enter the length of rectangle B:'))
Width_B = int(input('Enter the width of rectangle B:'))

#Calculate the area of each rectangle and assign variables
Area_A = (Length_A * Width_A)
Area_B = (Length_B * Width_B)

#Output the area of each rectangle and print which one is larger or if they are equal
print('Area of rectangle A =', Area_A)
print('Area of rectangle B =', Area_B)

if Area_A > Area_B:
    print('Rectangle A is larger than rectangle B.')
elif Area_B > Area_A:
    print('Rectangle B is larger than rectangle A.')
else:
    print('The rectangles are the same size.')
