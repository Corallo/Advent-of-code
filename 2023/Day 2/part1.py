#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
session_id = open("Session", "r").read()
data = get_data(day=2, year=2023,session=session_id).split("\n")
#data = open("./Day 2/data", "r").read().split("\n")

print(data)
data= [line.replace(":", ";").split(";")[1:] for line in data]

max_red = 12
max_green = 13
max_blue = 14

score = 0
for idx, line in enumerate(data):
    print(idx+1, line)
    bad_game = False
    for extraction in line:
        if not bad_game:
            for color in extraction.split(","):
                if "red" in color and int(color.replace("red", "")) > max_red:
                        bad_game = True
                        break
                elif "green" in color and int(color.replace("green", "")) > max_green:
                        bad_game = True
                        break
                elif "blue" in color and int(color.replace("blue", "")) > max_blue:
                        bad_game = True
                        break
    if not bad_game:
        score += idx+1
answer = score


print(answer)
submit(answer, part="a", day=2, year=2023, session=session_id)
