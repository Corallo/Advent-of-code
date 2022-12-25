#read file
with open("Day 18/input.txt") as f:
    lines = f.readlines()


lines = [line.strip().split(",") for line in lines]
lines = [[int(line[0]), int(line[1]), int(line[2])] for line in lines]

faces = [6]*len(lines)
for cube in lines:
    #if there's another cube adjacent to it, remove a face
    for other_cube in lines:
        if other_cube != cube:
            if abs(cube[0] - other_cube[0]) + abs(cube[1] - other_cube[1]) + abs(cube[2] - other_cube[2]) <= 1:
                faces[lines.index(cube)] -= 1
print(sum(faces))