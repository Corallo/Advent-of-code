from aocd.models import Puzzle

YEAR = 2023
DAY = 3
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#data = puzzle.examples[0][0]

print(data)

data=data.split("\n")

print(len(data), len(data[0]))
#Find coordinates of all symbols
coord = []
for y in range(len(data)):
    for x in range(len(data[y])):
        if  data[y][x] == "*":
            coord.append((y,x))

new_coord = []
#Filter only coord that have two numbers around them
for c in coord:
    y = c[0]
    x = c[1]
    count = 0
    if x-1 >= 0 and data[y][x-1].isdigit():
        count += 1
    if x+1 < len(data[y]) and data[y][x+1].isdigit():
        count += 1
    if y-1 >= 0:
        if data[y-1][x].isdigit():
            count += 1
        else:
            if x-1 >= 0 and data[y-1][x-1].isdigit():
                count += 1
            if x+1 < len(data[y-1]) and data[y-1][x+1].isdigit():
                count += 1
    if y+1 < len(data):
        if data[y+1][x].isdigit():
            count += 1
        else:
            if x-1 >= 0 and data[y+1][x-1].isdigit():
                count += 1
            if x+1 < len(data[y+1]) and data[y+1][x+1].isdigit():
                count += 1
    if count == 2:
        new_coord.append(c)
print(new_coord)
coord = new_coord
#for each coordinate, find all the adjacent numbers, sum them and replace them with .

sum_value = 0
for c in coord:
    y = c[0]
    x = c[1]
    value_prod = 1
    for y1 in range(y-1, y+2):
        for x1 in range(x-1, x+2):
            if y1 >= 0 and y1 < len(data) and x1 >= 0 and x1 < len(data[y1]):
                if data[y1][x1].isdigit():
                    start_digit  = x1
                    end_digit = x1
                    # walk left until you find a non digit
                    for x2 in range(x1-1, -1, -1):
                        if data[y1][x2].isdigit():
                            start_digit = x2
                        else:
                            break
                    # walk right until you find a non digit
                    for x2 in range(x1+1, len(data[y1])):
                        if data[y1][x2].isdigit():
                            end_digit = x2
                        else:
                            break
                    value = int(data[y1][start_digit:end_digit+1])
                    value_prod *= value
                    data[y1] = data[y1][:start_digit] + "."*(end_digit-start_digit+1) + data[y1][end_digit+1:]
    sum_value += value_prod
print(sum_value)
puzzle.answer_b = sum_value