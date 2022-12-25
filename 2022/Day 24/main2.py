import networkx as nx
from tqdm import tqdm
#read file
with open("Day 24/test.txt") as f:
     data = f.readlines()
    
data = [line.strip() for line in data]
#find max x and y
max_x = len(data[0])-2
max_y = len(data)-2
min_x = 1
min_y = 1

print(min_x,max_x,min_y,max_y)

#find coordinates of all > < ^ v in the map
blizzards = set()
id=0
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char in ["<", ">", "^", "v"]:
            #add to set
            blizzards.add((x,y,char))

start_position = (1,0)
end_position = (data[-1].find("."),len(data)-1)

#Update blizzards positions
def update_blizzards_positions(blizzards):
    new_blizzards = set()
    for element in blizzards:
        if element[2] == ">":
            new_position = (element[0]+1, element[1])
            if new_position[0] > max_x:
                new_position = (min_x, new_position[1])
        elif element[2] == "<":
            new_position = (element[0]-1, element[1])
            if new_position[0] < min_x:
                new_position = (max_x, new_position[1])
        elif element[2] == "^":
            new_position = (element[0], element[1]-1)
            if new_position[1] < min_y:
                new_position = (new_position[0], max_y)
        elif element[2] == "v":
            new_position = (element[0], element[1]+1)
            if new_position[1] > max_y:
                new_position = (new_position[0], min_y)
        new_blizzards.add((new_position[0], new_position[1], element[2]))
    return new_blizzards

def check_position(blizzards, position):
    if (position[0], position[1], ">") in blizzards:
        return ">"
    if (position[0], position[1], "<") in blizzards:
        return "<"
    if (position[0], position[1], "^") in blizzards:
        return "^"
    if (position[0], position[1], "v") in blizzards:
        return "v"
    return "."

def print_map(blizard_positions):
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "#":
                print("#", end="")
            else:
                print(check_position(blizard_positions, (x,y)), end="")
        print()

def get_neighbor(position):
    neighbors = []
    if position[1] == 0 and position[0] == 1: #Special case start position
        return [position,(1,1)]
    if position[1] == 1 and position[0] == 1: #Special case start position
        neighbors.append((1,0))
    if position[1] == max_y and position[0] == max_x: #Special case end position
        neighbors.append((max_x, max_y+1))
    if position[1] == (max_y+1) and position[0] == min_x: #Special case end position
        return[position,(min_x, max_y)]
    if position[0] < max_x:
        neighbors.append((position[0]+1, position[1]))
    if position[0] > min_x:
        neighbors.append((position[0]-1, position[1]))
    if position[1] < max_y:
        neighbors.append((position[0], position[1]+1))
    if position[1] > min_y:
        neighbors.append((position[0], position[1]-1))
    neighbors.append((position[0], position[1]))
    return neighbors

#Generate graph
G = nx.DiGraph()

t_max_total = 1000

print("Generating graph")
for t in tqdm(range(t_max_total)):
    new_blizzards = update_blizzards_positions(blizzards)

    for i in range(0, len(data[0])):
        for j in range(0, len(data)):
            if data[j][i] == "#":
                continue
            if check_position(blizzards, (i,j)) == ".":
                for n in get_neighbor((i,j)):
                    if check_position(new_blizzards, n) == ".":
                        G.add_edge((i,j,t), (n[0],n[1],t+1), weight=1)
    if t==274 or t==683:
        print()
        print_map(blizzards)
    
    blizzards = new_blizzards

print("Searching for solution way 1")
t_min = 1
t_max = t_max_total


while t_min < t_max:
    t = (t_min+t_max)//2
    if nx.has_path(G, start_position+(0,), end_position+(t,)):
        t_max = t
    else:
        t_min = t+1

going_back_time = t_max
print("Best time for path 1: ", t_max)


print("Searching for solution way back")
t_min = going_back_time+1
t_max = t_max_total


while t_min < t_max:
    t = (t_min+t_max)//2
    if nx.has_path(G, end_position+(going_back_time,), start_position+(t,)):
        t_max = t
    else:
        t_min = t+1
print("Best time for way back: ", t_max)
going_goal_2 = t_max


print("Searching for solution way 2")
t_min = going_goal_2+1
t_max = t_max_total

while t_min < t_max:
    t = (t_min+t_max)//2
    if nx.has_path(G, start_position+(going_goal_2,), end_position+(t,)):
        t_max = t
    else:
        t_min = t+1

print("Best time for path 2: ", t_max)
