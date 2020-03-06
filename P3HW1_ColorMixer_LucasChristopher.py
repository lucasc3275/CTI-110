#CTI-110
#P3HW1-Color Mixer
#Christopher Lucas
#March 3, 2020

#Obtain color input from user and assign variables Color1 & Color2.
#If the color combination is red or blue then display purple
#Elif the color combination is red and yellow then display orange
#Elif the color combinaiton is blue and yellow then diplay
#Else display error message saying both colors must be primary

color1=input('Please enter 1st primary color:')
color2=input('Please enter 2nd primary color:')

print()

if color1=='red' and color2=='blue' or color1=='blue' and color2=='red':
    print('Your color mix is Purple')

elif color1=='red' and color2=='yellow' or color1=='yellow' and color2=='red':
    print('Your color mix is Orange')

elif color1=='blue' and color2=='yellow' or color1=='yellow' and color2=='blue':
    print('Your color mix is Green')

else:
    print('Error: Both colors must be primary colors!')
