#from ..input_parser import get_data
from aocd import get_data
from aocd import submit

session_id = open("Session", "r").read()
data = get_data(day=7, year=2025, session=session_id)
#with open("./2025/day 7/data.txt", "r") as f:
#    data = f.read()
print(data)
data = data.splitlines()
print(data)

# find start coordinates
start = (0,0)
for i in range(len(data[0])):
    if data[0][i] == "S":
        start = (0,i)
        break
print(f"Start coordinates: {start}")
beams = [start]

def all_beams_are_done(beams):
    for beam in beams:
        x, y = beam
        if x < len(data)-1:
            return False
    return True
counter = 0

while not all_beams_are_done(beams):
    new_beams = set()
    for beam in beams:
        x, y = beam
        if x + 1 < len(data):
            if data[x+1][y] == ".":
                beam = (x+1, y)
                new_beams.add(beam)
            elif data[x+1][y] == "^":
                counter += 1
                new_beams.add((x+1, y+1))
                new_beams.add((x+1, y-1))
    beams = new_beams
      
print(counter)
submit(counter, part="a", day=7, year=2025, session=session_id)