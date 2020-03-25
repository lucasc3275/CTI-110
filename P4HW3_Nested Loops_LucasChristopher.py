#This program will use nested loops to draw a pattern.
#CTI-110
#P4HW3-Nested Loops
#March 24, 2020
#Christopher Lucas

#assign the range value to the variable 'steps'
#use the for loop in range 'steps
    #display # for 6 lines
    #nest variable 'c' in range 'r'
        #display spaces to iterate 6 times
    #print # in original loop

steps=6

for r in range(steps):
    print('#', end='')
    for c in range (r):
        print('  ' , end='')
    print('#')