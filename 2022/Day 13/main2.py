#read input
with open('./Day 13/input_2.txt') as f:
    lines = f.read()

#split by double newline
lines = lines.split('\n')

#apply eval() to each line
lines = [eval(line) for line in lines]

#Recursivly compare each pair of lines
#If both values are integers, the lower integer should come first. 
#If the left integer is lower than the right integer, the inputs are in the right order. 
#If the left integer is higher than the right integer, the inputs are not in the right order. 
#Otherwise, the inputs are the same integer; continue checking the next part of the input.
#If both values are lists, compare the first value of each list, then the second value, and so on. 
#If the left list runs out of items first, the inputs are in the right order. 
#If the right list runs out of items first, the inputs are not in the right order. 
#If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
#If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison. 
#For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].
def compare(line1, line2):
    #if both are integers
    if type(line1) == int and type(line2) == int:
        #if left is lower
        if line1 < line2:
            return 1
        #if right is lower
        elif line1 > line2:
            return -1
        #if they are the same
        else:
            return 0
    #if both are lists
    elif type(line1) == list and type(line2) == list:
        for i in range(min(len(line1), len(line2))):
            #compare first value
            result = compare(line1[i], line2[i])
            #if not the same
            if result != 0:
                return result
        #if they are the same
        if len(line1) == len(line2):
            return 0
        #if left is shorter
        elif len(line1) < len(line2):
            return 1
        #if right is shorter
        else:
            return -1
        
    #if one is integer and one is list
    elif type(line1) == int and type(line2) == list:
        #convert integer to list
        return compare([line1], line2)
    elif type(line1) == list and type(line2) == int:
        #convert integer to list
        return compare(line1, [line2])
    
#add "[[2]]" and "[[6]]"
lines.append([[2]])
lines.append([[6]])

#sort lines
from functools import cmp_to_key
lines.sort(key=cmp_to_key(lambda item1, item2: compare(item1,item2)), reverse=True)
print(lines)
#find position of "[[2]]" and "[[6]]"
x1=lines.index([[2]])
x2=lines.index([[6]])

print((x1+1)*(x2+1))

"""
cout = 0
for i in range(len(lines)):
    if(compare(lines[i][0], lines[i][1])):
        cout += i+1
        print("Correct",lines[i])
print(cout)
"""
