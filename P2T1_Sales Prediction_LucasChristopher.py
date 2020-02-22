#This program will predict yearly profit based on projected annual sales.
#February 8, 2020
#CTI-110 P2T1-Sales Prediction
#Christopher Lucas

#Get the projected total sales.
total_sales=float(input('Enter the projected sales:'))

#Calculate the profit as 23 percent of total sales.
profit=total_sales * 0.23

#Display the profit.
print('The profit is $', format (profit, ',.2f'),sep='')
