import re
from tqdm import tqdm
import ranges 
#Also this took 4 attempts to get right, take almost 1h to solve the problem
#Read input
with open('./Day 15/input.txt') as f:
    lines = f.readlines()
#target_y = 2000000
x_limit = 4000000
y_limit = 4000000
x_start = 0
y_start = 0

#Extract 4 numbers
lines = [re.findall(r'-?\d+', line) for line in lines]
#make int
lines = [[int(x) for x in line] for line in lines]

for target_y in tqdm(range(y_start,y_limit)):
    full_range = ranges.RangeSet()
    for line in lines:
        #get start and end
        S = line[:2]
        B = line[2:]
        
        #Calcolate manatthan distance between S and B
        manhattan_distance = abs(S[0]-B[0]) + abs(S[1]-B[1])
        distance_to_target_y = abs(S[1]-target_y)
        #Calcolate the number of # to insert
        number_of_sharp = (manhattan_distance - distance_to_target_y)  
        #Add  number_of_sharp '#' to matrix_line in position S[1]
        if number_of_sharp >= 0:
            full_range.add(ranges.Range(S[0]-number_of_sharp, S[0]+number_of_sharp+1))


    full_range=full_range.intersection(ranges.Range(0, x_limit))
    if full_range != ranges.Range(0, x_limit):
        print("Line ", target_y ,full_range)
        break

