#This program keeps a running total of bugs collected over a 7 day period
#March 20, 2020
#CTI-110 P4T2-Bug Collector
#Christopher Lucas

#set accumulator to 0 and assign variable "total_bugs"
#for 7 days: prompt user to enter the number of bugs collected each day
#add the daily number of bugs to the accumulator
#display total of bugs for the week

total_bugs=0

for day in range(1, 8):
    print('Enter the amount of bugs collected on day', day,':')
    bugs=int(input())
    total_bugs += bugs
    
print('You collected', total_bugs, 'bugs for the week')