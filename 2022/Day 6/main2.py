#read input
with open('./Day 6/input.txt') as f:
    line = f.readlines()

line = line[0]

#find position the first group of 4 different characters

for i in range(len(line)):
    #check 4 characters of line are all unique
    if len(set(line[i:i+14])) == 14:
        print(i+14)
        print(line[i:i+14])
        break
