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
    #append to crates(line[2]) the last n element of crates(line[1])
    crates[line[2]-1].extend(crates[line[1]-1][-line[0]:])
    #remove last n elements from crate 1
    crates[line[1]-1] = crates[line[1]-1][:-line[0]]
    print(crates)

#print last of each crates

for crate in crates:
    print(crate[-1])
    