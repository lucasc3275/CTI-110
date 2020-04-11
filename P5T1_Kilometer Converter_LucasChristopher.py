#This program will take a user input value in kilometers and convert it to miles.
#April 9, 2020
#CTI-110 P5T1_Kilometer Converter
#Christopher Lucas

#Assign global constant to conversion factor of 0.6214
#Main function obtains user input and assigns variable 'kilometers'
#then calls show_miles function using 'kilometers' as an argument
#Show_miles function call the 'km' input from main function and
#then converts kilometers into mile using the global constant
#Display the converted miles
#Call the main function

CONVERSION_FACTOR=0.6214

def main ():
    kilometers=float(input('Enter the number of kilometers to be converted: '))
    show_miles(kilometers)
    
def show_miles(km):
    miles = km * CONVERSION_FACTOR
    print(km, 'kilometers equals' , format(miles, ',.3f'), 'miles.')
    
main()