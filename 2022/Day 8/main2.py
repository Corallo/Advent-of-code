#read input matrix
with open('./Day 8/input.txt') as f:
    lines = f.readlines()


#convert to list of lists
lines = [line.strip() for line in lines]

#convert to list of lists of one char int
tree_map = [[int(x) for x in line] for line in lines]

def check_visibility_score(tree_map, x, y):
    #check if from x,y we can see the tree
    #check if it is visible on the left
    tree_value = tree_map[y][x]
    visibility_nord=0
    visibility_sud=0
    visibility_est=0
    visibility_west=0
    for i in range(x-1, -1, -1):
        visibility_west+=1 
        if tree_map[y][i] >= tree_value:
            break
    for i in range(x+1, len(tree_map[y])):
        visibility_est += 1
        if tree_map[y][i] >= tree_value:
            break
    for i in range(y-1, -1, -1):
        visibility_nord += 1
        if tree_map[i][x] >= tree_value:
            break
    for i in range(y+1, len(tree_map)):
        visibility_sud += 1
        if tree_map[i][x] >= tree_value:
            break
    return visibility_nord * visibility_sud * visibility_est * visibility_west
    
count=0
visibility_map = [[0 for x in range(len(tree_map[y]))] for y in range(len(tree_map))]
#find tree with highest visibility score
max_score = 0
max_score_pos = (0,0)
for y in range(1,len(tree_map)-1):
    for x in range(1,len(tree_map[y])-1):
        score = check_visibility_score(tree_map, x, y)
        if score > max_score:
            max_score = score
            max_score_pos = (x,y)
print(max_score_pos)
print(max_score)

    