#Read input
with open('./Day 9/real_input.txt') as f:
    lines = f.readlines()

#parse char and int for eavh line
lines = [x.strip().split(' ') for x in lines]
print(lines)

head_position = (0,0)
tail_position = (0,0)

visited = set()
visited.add(tail_position)

for line in lines:
    #parse direction and distance
    direction = line[0]
    distance = int(line[1])
    print(direction, distance)
    print("head position: ", head_position)
    print("tail position: ", tail_position)
    print("moving head")
    for i in range(distance):
        if direction == 'R':
            head_position = (head_position[0]+1, head_position[1])
        elif direction == 'L':
            head_position = (head_position[0]-1, head_position[1])
        elif direction == 'U':
            head_position = (head_position[0], head_position[1]+1)
        elif direction == 'D':
            head_position = (head_position[0], head_position[1]-1)
       
        #check if tail is adjacent to head
        if not ((tail_position[0]-head_position[0])**2 <=1 and  (tail_position[1]-head_position[1])**2 <= 1):
            print("tail is not adjacent to head, pulling tail")
            if tail_position[0] < head_position[0]:
                tail_position = (tail_position[0]+1, tail_position[1])
            if tail_position[0] > head_position[0]:
                tail_position = (tail_position[0]-1, tail_position[1])
            if tail_position[1] < head_position[1]:
                tail_position = (tail_position[0], tail_position[1]+1)
            if tail_position[1] > head_position[1]:
                tail_position = (tail_position[0], tail_position[1]-1)
        else:
            print("tail is adjacent to head")
        print("head position: ", head_position)
        print("tail position: ", tail_position)
        visited.add(tail_position)


print("visited: ", visited)
print(len(visited))