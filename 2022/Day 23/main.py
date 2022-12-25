import matplotlib.pyplot as plt
import time
#read file
with open("Day 23/input.txt") as f:
    data = f.readlines()

data = [line.strip() for line in data]
elfs_positions = []

#find coordinates of all # in the map
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == "#":
            elfs_positions.append((x,y))

directions = ["N", "S", "W", "E"]

def check_direction(elf, dir):
    if dir == "N":
        if      (elf[0]  , elf[1] - 1) not in elfs_positions \
           and ((elf[0]-1, elf[1] - 1) not in elfs_positions) \
           and ((elf[0]+1, elf[1] - 1) not in elfs_positions):
            return True
    elif dir == "S":
        if      ((elf[0]  , elf[1] + 1) not in elfs_positions) \
            and ((elf[0]-1, elf[1] + 1) not in elfs_positions) \
            and ((elf[0]+1, elf[1] + 1) not in elfs_positions):
            return True
    elif dir == "W":
        if     ((elf[0] - 1, elf[1]  ) not in elfs_positions) \
           and ((elf[0] - 1, elf[1]-1) not in elfs_positions) \
           and ((elf[0] - 1, elf[1]+1) not in elfs_positions):
            return True
    elif dir == "E":
        if ((elf[0] + 1, elf[1]  ) not in elfs_positions) \
           and ((elf[0] + 1, elf[1]-1) not in elfs_positions) \
           and ((elf[0] + 1, elf[1]+1) not in elfs_positions):
            return True

def draw_map(elfs_positions):
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if (x,y) in elfs_positions:
                print("#", end="")
            else:
                print(".", end="")
        print()

#Check if there is another elf in the neighborhood
def check_free_neighboorhood(elf):
    if (elf[0] -1, elf[1] - 1) in elfs_positions or \
       (elf[0]   , elf[1] - 1) in elfs_positions or \
       (elf[0] +1, elf[1] - 1) in elfs_positions or \
       (elf[0] -1, elf[1] + 1) in elfs_positions or \
       (elf[0]   , elf[1] + 1) in elfs_positions or \
       (elf[0] +1, elf[1] + 1) in elfs_positions or \
       (elf[0] - 1, elf[1]  ) in elfs_positions or \
       (elf[0] + 1, elf[1]  ) in elfs_positions:
        return False
    return True 

def draw_graphic_map(elfs_positions):
    min_x = min([x for x,y in elfs_positions])
    max_x = max([x for x,y in elfs_positions])
    min_y = min([y for x,y in elfs_positions])
    max_y = max([y for x,y in elfs_positions])
    elf_map = []
    for y in range(min_y, max_y+1):
        l = []
        for x in  range(min_x, max_x+1):
            if (x,y) in elfs_positions:
                l.append(1)
            else:
                l.append(0)
        elf_map.append(l)
    plt.imshow(elf_map)
    plt.ion()
    plt.show()
    plt.pause(.001)


rounds = 0
#draw_map(elfs_positions)


for r in range(rounds):
    print("Round", r+1)
    #print(len(elfs_positions), "elfs")
    elf_new_positions = []
    for elf in elfs_positions:
        if check_free_neighboorhood(elf):
                elf_new_positions.append(elf)
                continue
        moving = False
        for dir in directions:
            if check_direction(elf, dir):
                moving = True
                if dir == "N":
                    elf_new_positions.append((elf[0], elf[1] - 1))
                elif dir == "S":
                    elf_new_positions.append((elf[0], elf[1] + 1))
                elif dir == "W":
                    elf_new_positions.append((elf[0] - 1, elf[1]))
                elif dir == "E":
                    elf_new_positions.append((elf[0] + 1, elf[1]))
                break
        if not moving:
            elf_new_positions.append(elf)
    #find index of elfs on the same position
    for i, elf in enumerate(elf_new_positions):
        if elf in elf_new_positions[i+1:]:
            elf_new_positions[i] = elfs_positions[i]
            #remove also the other elf
            list_idx = [j for j, x in enumerate(elf_new_positions) if x == elf]
            for j in list_idx:
                elf_new_positions[j] = elfs_positions[j]
    if elfs_positions == elf_new_positions:
        break
    elfs_positions = elf_new_positions
    #rotate directions
    directions = directions[1:] + directions[:1]
    draw_map(elfs_positions)
    draw_graphic_map(elfs_positions)

#find min and max of x and y
min_x = min([x for x,y in elfs_positions])
max_x = max([x for x,y in elfs_positions])
min_y = min([y for x,y in elfs_positions])
max_y = max([y for x,y in elfs_positions])
print(min_x, max_x, min_y, max_y, len(elfs_positions))
#count "." in the map
count = (max_x - min_x + 1) * (max_y - min_y + 1) - len(elfs_positions)
print("Result", count)

time.sleep(10)
        
