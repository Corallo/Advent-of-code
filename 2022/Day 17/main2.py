
from tqdm import tqdm
#Runt this to produce delta file, then run pattern_finder.py
#read file
with open('./Day 17/input.txt') as f:
    lines = f.readlines()

number_of_rocks = 10000000

rocks = [[(0,0), (1,0), (2,0), (3,0)],        # ----
         [(0,1), (1,1), (2,1), (1,0), (1,2)], # +
         [(0,0), (1,0), (2,0), (2,1), (2,2)], # L
         [(0,0), (0,1), (0,2), (0,3)],        # |
         [(0,0), (0,1), (1,0), (1,1)]]        # []



# convert list of string into list of chars
lines = [list(line.strip()) for line in lines]
gaiser_list = lines[0]
print(gaiser_list)
print(len(gaiser_list))



mapp = set()

rock_shapes=rocks
def get_rock_w(rock):
    return max([x for x,y in rock]) +1

def check_collision(mapp, rock, pos, map_bottom):
    x, y = pos
    if y < map_bottom:
        return True
    if x < 0 or x + get_rock_w(rock) > 7:
        return True
    for coord in rock:
        if (coord[0]+x, coord[1]+y) in mapp:
            return True
    return False
def print_tower_rock(tower, rock, pos, towerheight):
    rockbottom = pos[1]
    rockleft = pos[0]
    h = towerheight + 8
    w = 7
    grid = [['.' for x in range(w)] for y in range(h)]
    for coord in rock:
        grid[coord[1]+rockbottom][coord[0]+rockleft] = "@"
    for key in tower:
        grid[key[1]][key[0]] = "#"
    for y in range(len(grid)-1, -1, -1):
            print(*grid[y])
    print()

map_bottom = 0
size = 0
gaiser_index = 0
n_rock=0
chace = {}
old_size = 0
for n_rock in tqdm(range(number_of_rocks)):
    rock = rock_shapes[n_rock%len(rock_shapes)]
    #Place the rock 2 square from the left and 3 squares from the bottom
    rock_position = [2, size+3]
    touch = False
    while not touch:
        #print_tower_rock(mapp, rock, rock_position, size)

        old_pos = rock_position.copy()
        gaiser = gaiser_list[gaiser_index]
        if gaiser == '>':
            rock_position[0] += 1
        elif gaiser == '<':
            rock_position[0] -= 1
        if check_collision(mapp, rock, rock_position, map_bottom):
            rock_position = old_pos.copy()
        gaiser_index = (gaiser_index + 1) % len(gaiser_list)
        old_pos = rock_position.copy()
        rock_position[1] -= 1
        if check_collision(mapp, rock, rock_position, map_bottom):
            rock_position[1] += 1
            touch = True
            
            for pos in rock:
                #add to pos to mapp
                mapp.add((pos[0]+rock_position[0], pos[1]+rock_position[1]))
                size = max(size, rock_position[1]+pos[1]+1)
            break
    #append new size to file
    with open('./Day 17/delta.txt', 'a') as f:
        f.write(str(size-old_size) + '\n')
    old_size = size


    