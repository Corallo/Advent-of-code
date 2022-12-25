import numpy as np
#Read file

with open('./Day 14/input.txt') as f:
    lines = f.readlines()

#split lines with -> and strip
lines = [line.strip().split(' -> ') for line in lines]

# split line with two pair divided by ,
lines = [[pair.split(',') for pair in line] for line in lines]

#make int
lines = [[[int(x) for x in pair] for pair in line] for line in lines]

print(lines)

#crate matrix
x_max = max([max([pair[0] for pair in line]) for line in lines])
y_max = max([max([pair[1] for pair in line]) for line in lines])
matrix = [['.' for x in range(x_max+1)] for y in range(y_max+1)]

#fill matrix
for line in lines:
    #draw a line from pair i to pair i+1
    for i in range(len(line)-1):
        #get start and end
        start = line[i]
        end = line[i+1]
        #get direction
        if start[0] == end[0]:
            #vertical
            if start[1] < end[1]:
                #down
                for y in range(start[1], end[1]+1):
                    matrix[y][start[0]] = '#'
            else:
                #up
                for y in range(end[1], start[1]+1):
                    matrix[y][start[0]] = '#'
        else:
            #horizontal
            if start[0] < end[0]:
                #right
                for x in range(start[0], end[0]+1):
                    matrix[start[1]][x] = '#'
            else:
                #left
                for x in range(end[0], start[0]+1):
                    matrix[start[1]][x] = '#'

def show_matrix(matrix):
    display_matrix = np.array(matrix)[:,493:]
    print(display_matrix)

show_matrix(matrix)


# Drop sand from top column 500, it falls down, 
# if it touches a # it tries to go down left
# if it can't, it tries to go down right,
# if it can't it stops. 

i=0
while True:
    print(i)
    i+=1
    #spawn a new sand in 500,0
    sand_pos = [500,0]
    not_moved = False
    while not not_moved:
        not_moved = True
        #while sand is not blocked
        while matrix[sand_pos[1]+1][sand_pos[0]] == '.':
            #move down
            sand_pos[1] += 1
            not_moved = False
        while matrix[sand_pos[1]+1][sand_pos[0]] != '.' and \
        matrix[sand_pos[1]+1][sand_pos[0]-1] == '.':
            # move down left
            sand_pos[1] += 1
            sand_pos[0] -= 1
            not_moved = False

        while matrix[sand_pos[1]+1][sand_pos[0]] != '.' and \
            matrix[sand_pos[1]+1][sand_pos[0]-1] != '.' and \
            matrix[sand_pos[1]+1][sand_pos[0]+1] == '.':
            # move down right
            sand_pos[1] += 1
            sand_pos[0] += 1
            not_moved = False
    #fill matrix with sand
    matrix[sand_pos[1]][sand_pos[0]] = 'o'
    

#Code will crash when sand falls into the void,
#it doesn't matter, we care about the last valid i
    



show_matrix(matrix)


