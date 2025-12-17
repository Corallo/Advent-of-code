#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
import numpy as np
import re

session_id = open("Session", "r").read()
data = get_data(day=12, year=2025, session=session_id)
#with open("./2025/day 11/data.txt", "r") as f:
#    data = f.read()
data = data.split("\n\n")
pieces = [data[0].splitlines()[1:], data[1].splitlines()[1:], data[2].splitlines()[1:], data[3].splitlines()[1:],data[4].splitlines()[1:], data[5].splitlines()[1:]]
regions = data[6].splitlines()
print ("pieces:", pieces)

re = re.compile(r"(\d+)x(\d+): (\d+) (\d+) (\d+) (\d+) (\d+) (\d+)")
regions = [re.match(line) for line in regions]
regions = [(int(match.group(1)), int(match.group(2)), [int(match.group(i)) for i in range(3, 9)]) for match in regions]
print("regions:", regions)

easy_regions = 0
hard_regions = 0
impossible_regions = 0
pieces_size = [sum(line.count("#") for line in piece) for piece in pieces]
print("pieces size:", pieces_size)

pieces_size=np.array(pieces_size)
for region in regions:
    requirement= np.array(region[2])
    region_area = region[0] * region[1]
    if region_area >= 9*sum(requirement): # all pieces can fit without squeezing
        easy_regions += 1
    elif region_area > sum(requirement*pieces_size): # all pieces can fit with squeezing
        hard_regions += 1
        print(region_area-sum(requirement*pieces_size))
    else: # no way to fit all pieces
        impossible_regions += 1

print("easy regions:", easy_regions)
print("hard regions:", hard_regions)
print("impossible regions:", impossible_regions)


#submit(easy_regions, part="a", day=12, year=2025, session=session_id)