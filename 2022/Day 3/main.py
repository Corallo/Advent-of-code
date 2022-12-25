#Read file
with open('./Day 3/input.txt') as f:
    lines = f.readlines()

lowercase = [chr(x) for x in range(ord('a'),ord('z')+1)]

#Generate mapping
mapping = dict(zip(lowercase,map(lambda x:ord(x)-96,lowercase)))

score = 0
matches = []
#for each line, find which char is repeated in the first and second half of the line
for line in lines:
    part1 = line[:-len(line)//2]
    part2 = line[len(line)//2:]

    res = set(part1).intersection(part2)
    element  = list(res)[0]
    if element.isupper():
        score += 26
    score += mapping[element.lower()]

print(score)