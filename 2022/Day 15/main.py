import re
from tqdm import tqdm
#Final version, 4th attempt to solve this.

#Read input
with open('./Day 15/input.txt') as f:
    lines = f.readlines()
target_y=2000000
#Extract 4 numbers
lines = [re.findall(r'-?\d+', line) for line in lines]
#make int
lines = [[int(x) for x in line] for line in lines]

#crate matrix
x_max = max([line[0] for line in lines])
x_max_2 = max([line[2] for line in lines])
y_max = max([line[1] for line in lines])
y_max_2 = max([line[3] for line in lines])
x_max = max(x_max, x_max_2)
y_max = max(y_max, y_max_2)

#find x,y min
x_min = min([line[0] for line in lines])
x_min_2 = min([line[2] for line in lines])
y_min = min([line[1] for line in lines])
y_min_2 = min([line[3] for line in lines])
x_min = min(x_min, x_min_2)
y_min = min(y_min, y_min_2)

#Normalize coordinates
lines = [[line[0]-x_min, line[1]-y_min, line[2]-x_min, line[3]-y_min] for line in lines]

#add x_min and y_min to x_max and y_max
x_max += abs(x_min)
y_max += abs(y_min)
target_y += abs(y_min)

#matrix = [['.' for x in range(x_max+1)] for y in range(y_max+1)]
matrix_line = ['.' for x in range(x_max+1)]
#fill matrix
#Insert S in line[0],line[1] and B in line[2],line[3]
#Then, draw # expanding from S to B

sharp_set = set()
sharp_count = 0
beacon_in_line = 0

for line in tqdm(lines):
    #get start and end
    S = line[:2]
    B = line[2:]
    print([S[0]+x_min, S[1]+y_min], [B[0]+x_min, B[1]+y_min])
    if B[1]==target_y and B[0] not in sharp_set:
        sharp_set.add(B[0])
        beacon_in_line += 1
    
    #Calcolate manatthan distance between S and B
    manhattan_distance = abs(S[0]-B[0]) + abs(S[1]-B[1])
    print("Manhattan distance: ", manhattan_distance)
    distance_to_target_y = abs(S[1]-target_y)
    print("Distance to target y: ", distance_to_target_y)
    #Calcolate the number of # to insert
    number_of_sharp = (manhattan_distance - distance_to_target_y)  
    print("Number of sharp to add: ", number_of_sharp)
    #Add  number_of_sharp '#' to matrix_line in position S[1]
    for i in range(number_of_sharp+1):
        sharp_set.add(S[0]+i)
        sharp_set.add(S[0]-i)

    #print size of sharp set
    print(beacon_in_line)
    sharp_count = len(sharp_set) - beacon_in_line
    print("Sharp count: ", sharp_count)


        
#Count # in line 10
print(sharp_count)
