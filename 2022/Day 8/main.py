#read input matrix
with open('./Day 8/input.txt') as f:
    lines = f.readlines()


#convert to list of lists
lines = [line.strip() for line in lines]

#convert to list of lists of one char int
tree_map = [[int(x) for x in line] for line in lines]

def check_visibility(tree_map, x, y):
    #check if from x,y we can see the tree
    #check if it is visible on the left
    tree_value = tree_map[y][x]
    visibility_nord=True
    visibility_sud=True
    visibility_est=True
    visibility_west=True
    for i in range(x):
        if tree_map[y][i] >= tree_value:
            visibility_west = False
            break
    for i in range(x+1, len(tree_map[y])):
        if tree_map[y][i] >= tree_value:
            visibility_est = False
            break
    for i in range(y):
        if tree_map[i][x] >= tree_value:
            visibility_nord = False
            break
    for i in range(y+1, len(tree_map)):
        if tree_map[i][x] >= tree_value:
            visibility_sud = False
            break
    return visibility_nord or visibility_sud or visibility_est or visibility_west
    
count=0
visibility_map = [[0 for x in range(len(tree_map[y]))] for y in range(len(tree_map))]
for y in range(len(tree_map)):
    for x in range(len(tree_map[y])):
        if check_visibility(tree_map, x, y):
            count += 1
            print("visible ",x,y)
            visibility_map[y][x] = 1

print(count)

    