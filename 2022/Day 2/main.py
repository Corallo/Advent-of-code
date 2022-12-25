#read input file
with open('./Day 2/input.txt') as f:
    lines = f.readlines()


#take character 1 and 3 from each line
char1 = [line[0] for line in lines]
char2 = [line[2] for line in lines]

#convert x, Y, Z in A, B, C
char2 = [x.replace('X', 'A') for x in char2]
char2 = [x.replace('Y', 'B') for x in char2]
char2 = [x.replace('Z', 'C') for x in char2]

score = 0
for a,b in zip(char1,char2):
    score += ord(b) - ord('A') + 1
    #Draw
    if a == b:
        score +=3
    #Rock vs Scissors
    if b == 'A' and a == 'C':
        score += 6
    #Paper vs Rock
    if b == 'B' and a == 'A':
        score += 6
    #Scissors vs Paper
    if b == 'C' and a == 'B':
        score += 6

print(score)