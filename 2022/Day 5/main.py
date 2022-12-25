import re
#Read crates file
with open('./Day 5/input.txt') as f:
    lines = f.readlines()
with open('./Day 5/crates.txt') as f:
    crates = f.readlines()

#parse crates, remove newline and split by space
crates = [x.strip().split(' ') for x in crates]
print(crates)

#parse input, remove newline and extract numbers
data = [re.findall('\d+', line) for line in lines]

#convert to int
data = [[int(x) for x in line] for line in data]
print(data)

#Process crates

for line in data:
    for i in range(line[0]):
        crates[line[2]-1].append(crates[line[1]-1].pop())

#print last of each crates

for crate in crates:
    print(crate[-1])
    