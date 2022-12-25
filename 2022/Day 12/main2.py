from dijkstar import Graph, find_path
# read file
with open('./Day 12/input.txt') as f:
    lines = f.readlines()

# make list of list of chars
data = [list(line.strip()) for line in lines]
# make list of list of ints
data = [[ord(x) for x in line] for line in data]

# Find position of 83 (S) and (E) 
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 83:
            start = [i,j]
            data[i][j] = ord('a')
        if data[i][j] == 69:
            goal = [i,j]
            data[i][j] = ord('z')


adj_matrix = [[0 for x in range(len(data[0]*len(data)))] for y in range(len(data)*len(data[0]))]
h=len(data)
w=len(data[0])
#print(data)
# make adjacency matrix, it is traversable if adjiacent is <= current + 1

for i in range(len(data)):
    for j in range(len(data[i])):
        if j<w-1 and data[i][j+1] <= data[i][j]+1:
            adj_matrix[i*w+j][i*w+j+1] = 1
        if i<h-1 and data[i+1][j] <= data[i][j]+1:
            adj_matrix[(i)*w+j][(i+1)*w+j] = 1
        if j>0 and data[i][j-1] <= data[i][j]+1:
            adj_matrix[i*w+j][i*w+j-1] = 1
        if i>0 and data[i-1][j] <= data[i][j]+1:
            adj_matrix[(i)*w+j][(i-1)*w+j] = 1

#print(adj_matrix)

graph = Graph()
for i in range(len(adj_matrix)):
    for j in range(len(adj_matrix[i])):
        if adj_matrix[i][j] == 1:
            graph.add_edge(i, j, 1)

starts = []
#Find all starting point (a)
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 97:
            starts.append([i,j])

#try all starting points
paths = []
for start in starts:
    #ignore failurs
    try:
        #store path length
        paths.append(find_path(graph, start[0]*w+start[1], goal[0]*w+goal[1]).total_cost)
    except:
        pass

# print shorter path
print(min(paths))