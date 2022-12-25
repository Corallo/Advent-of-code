#Read input
with open('./Day 9/real_input.txt') as f:
    lines = f.readlines()

#parse char and int for eavh line
lines = [x.strip().split(' ') for x in lines]
print(lines)

nodes = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]

#nodes = [(0,0),(0,0)]


visited = set()
visited.add(nodes[-1])

for line in lines:
    #parse direction and distance
    direction = line[0]
    distance = int(line[1])
    print(direction, distance)
    print("head position: ", nodes[0])
    print("tail position: ", nodes[-1])
    print("moving head")
    for i in range(distance):
        if direction == 'R':
            nodes[0] = (nodes[0][0]+1, nodes[0][1])
        elif direction == 'L':
            nodes[0] = (nodes[0][0]-1, nodes[0][1])
        elif direction == 'U':
            nodes[0] = (nodes[0][0], nodes[0][1]+1)
        elif direction == 'D':
            nodes[0] = (nodes[0][0], nodes[0][1]-1)

        for j in range(1,len(nodes)):
        #check if tail is adjacent to head
            if not ((nodes[j][0]-nodes[j-1][0])**2 <=1 and  (nodes[j][1]-nodes[j-1][1])**2 <= 1):
                print("tail is not adjacent to head, pulling tail")
                if nodes[j][0] < nodes[j-1][0]:
                    nodes[j] = (nodes[j][0]+1, nodes[j][1])
                if nodes[j][0] > nodes[j-1][0]:
                    nodes[j] = (nodes[j][0]-1, nodes[j][1])
                if nodes[j][1] < nodes[j-1][1]:
                    nodes[j] = (nodes[j][0], nodes[j][1]+1)
                if nodes[j][1] > nodes[j-1][1]:
                    nodes[j] = (nodes[j][0], nodes[j][1]-1)
            else:
                print("tail is adjacent to head")
        print("head position: ", nodes[0])
        print("tail position: ", nodes[-1])
        visited.add(nodes[-1])


print("visited: ", visited)
print(len(visited))