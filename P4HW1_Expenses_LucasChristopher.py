#CTI-110
#P4HW1-Expenses
#Christopher Lucas
#March 21, 2020

#Instruct user to input beginning balance with assigned variable 'beg_balance'
#assign sentinal additional='y'
#assign accumulator for running monetary total of expenses and assign variable 'total_expense'
#assign accumulator for running total of the number of expenses and assign variable 'expense_num'
#while addtional = 'y' or 'Y'
    #instruct user to input first expense amount and assign variable 'expense'
    #add 1 to expense_num
    #add expense to total_expense
    #User inputs Y or N for any additional expenses, if 'y' or 'Y', loop continues
#subtract accumulated total_expense from beginning balance and assign variable 'balance'
#display beginning balance
#display the total number of expenses
#display the monetary total of expenses
#display the remaining balance

beg_balance=float(input('What is your beginning balance:$'))
additional='y'
expense_num=0
total_expense=0

while additional.lower() == 'y':
    expense=float(input('Enter expense:$'))
    expense_num+=1
    total_expense+=expense
    additional=input('Do you have any additional expenses?' + '(Enter Y/N):')

balance=(beg_balance-total_expense)

print('')

print('Amount in account prior to expenses:$', format(beg_balance, ',.2f'))
print('Number of expenses:', expense_num)
print('Total amount of expenses:$', format(total_expense, ',.2f'))
print('Remaining balance after expenses:$', format(balance, ',.2f'))
