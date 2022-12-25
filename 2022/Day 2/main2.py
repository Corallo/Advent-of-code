#read input file
with open('./Day 2/input.txt') as f:
    lines = f.readlines()


#take character 1 and 3 from each line
char1 = [line[0] for line in lines]
char2 = [line[2] for line in lines]

char3 = []
for a,b in zip(char1,char2):
    #You draw
    if b == 'Y':
        char3.append(a)
    #You win
    elif b == 'Z':
        val = 65 + (ord(a) - 65 + 1) % 3
        char3.append(chr(val))
    #You lose
    elif b == 'X':
        val = 65 + (ord(a) - 65 - 1) % 3
        char3.append(chr(val))

score = 0
for a,b in zip(char1,char3):
    score += ord(b) - ord('A') + 1
    #Draw
    if a == b:
        score +=3
    #Win condition
    if ord(b) - ord(a) == 1 or ord(b) - ord(a) == -2:
        score += 6

print(score)