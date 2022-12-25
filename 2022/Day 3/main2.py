#Read file
with open('./Day 3/input.txt') as f:
    lines = f.readlines()

lowercase = [chr(x) for x in range(ord('a'),ord('z')+1)]

#Generate mapping
mapping = dict(zip(lowercase,map(lambda x:ord(x)-96,lowercase)))

score = 0
matches = []
#for each line, find which char is repeated in the first and second half of the line
for i in range(len(lines)//3):
    line1 = lines[i*3][:-1]
    line2 = lines[(i*3)+1][:-1]
    line3 = lines[(i*3)+2][:-1]
    print(line1, line2, line3)
    
    res = set(line1).intersection(line2).intersection(line3)
    element  = list(res)[0]
    if element.isupper():
        score += 26
    score += mapping[element.lower()]
    
print(score)