#CTI-110
#P3LAB-Debugging
#Christopher Lucas
#March 11, 2020

#Have user input grade in integer form
#Define parameters for grades and assign variables
#If score 90 or above display your grade as an A
#Elif score 80 - 90, display your grade is a B
#Elif score 70 - 80, display your grade is a C
#Elif score 60 - 70, display your grade is a D
#Else display your grade is an F

score=int(input('What was your numbered score:'))
a_score=90
b_score=80
c_score=70
d_score=60

if score >= a_score:
    print('Your grade is an A')
elif score >= b_score:
    print('Your grade is a B')
elif score >= c_score:
    print('Your grade is a C')
elif score >= d_score:
    print('Your grade is a D')
else:
    print('Your grade is an F')