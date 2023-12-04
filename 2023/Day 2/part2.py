#from ..input_parser import get_data
from aocd import get_data
from aocd import submit

session_id = open("Session", "r").read()
data = get_data(day=2, year=2023,session=session_id).split("\n")
#data = open("./Day 2/data", "r").read().split("\n")

print(data)
data= [line.replace(":", ";").split(";")[1:] for line in data]


power = [0]*len(data)

score = 0
for idx, line in enumerate(data):
    print(idx+1, line)
    max_red = 0
    max_green = 0
    max_blue = 0
    for extraction in line:
            for color in extraction.split(","):
                if "red" in color and int(color.replace("red", "")) > max_red:
                        max_red = int(color.replace("red", ""))
                elif "green" in color and int(color.replace("green", "")) > max_green:
                        max_green = int(color.replace("green", ""))
                elif "blue" in color and int(color.replace("blue", "")) > max_blue:
                        max_blue = int(color.replace("blue", ""))
    print(max_red, max_green, max_blue)
    power[idx] = max_red * max_green * max_blue

print(power)
answer = sum(power)



print(answer)
submit(answer, part="b", day=2, year=2023, session=session_id)
