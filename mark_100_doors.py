"""
TODO: Some guy goes through the 100 doors and draws an X on 
every other door. He keeps making passes through the doors, 
skipping over doors that already have a X on them.
What’s the last door to get marked with an X?
Let’s pretend the 100 doors are in a circle

E.g. 
1st round: 2,4,6,8,...,98,100
2nd round: (skip 1), 3, (skip 5), 7,11,...,99
...

Data structures:
array for doors
boolean flag for skipping

Idea:
Loop from start
see if element value is 1 (marked), if 0 switch flag state
skip if flag is true
mark if door is 0 and flag is false
print the index
loop back to beginning when finish a round
"""
from collections import Counter

isSkipping = True
doors = {}
for i in range(1,101):
    doors[i] = 0
c = Counter(doors.values())

while(c[0] > 0):
    print("New Round: ")
    for i in range(1,101):
        #if door is marked
        if doors[i] == 1:
            continue
        else: # door is not marked, doors[i] = 0
            if isSkipping == True:
                isSkipping = False
                continue
            else:
                doors[i] = 1
                isSkipping = True
                print(i)
    #count number of zeros that's left
    c = Counter(doors.values())



        



