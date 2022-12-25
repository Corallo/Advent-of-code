#read input
with open('./Day 13/input.txt') as f:
    lines = f.read()

#split by double newline
lines = lines.split('\n\n')

#split by newline
lines = [line.split('\n') for line in lines]
#apply eval() to each line
lines = [[eval(line) for line in pair] for pair in lines]


#Recursivly compare each pair of lines
#If both values are integers, the lower integer should come first. If the left integer is lower than the right integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.
#If both values are lists, compare the first value of each list, then the second value, and so on. If the left list runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs are not in the right order. If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
#If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].
def compare(line1, line2):
    #if both are integers
    if type(line1) == int and type(line2) == int:
        #if left is lower
        if line1 < line2:
            return True
        #if right is lower
        elif line1 > line2:
            return False
        #if they are the same
        else:
            return None
    #if both are lists
    elif type(line1) == list and type(line2) == list:
        for i in range(min(len(line1), len(line2))):
            #compare first value
            result = compare(line1[i], line2[i])
            #if not the same
            if result != None:
                return result
        #if they are the same
        if len(line1) == len(line2):
            return None
        #if left is shorter
        elif len(line1) < len(line2):
            return True
        #if right is shorter
        else:
            return False
        
    #if one is integer and one is list
    elif type(line1) == int and type(line2) == list:
        #convert integer to list
        return compare([line1], line2)
    elif type(line1) == list and type(line2) == int:
        #convert integer to list
        return compare(line1, [line2])
    


cout = 0
for i in range(len(lines)):
    if(compare(lines[i][0], lines[i][1])):
        cout += i+1
        print("Correct",lines[i])
print(cout)

