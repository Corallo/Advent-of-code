from aocd.models import Puzzle
import numpy as np
from tqdm import tqdm
YEAR = 2023
DAY = 16
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#data = puzzle.examples[0][0]

data=data.splitlines()
print(data)

# "/" rotate 90 degree non-clockwise.
# If beam comes from left, it goes up. If beam comes from up, it goes left.
# if a beam comes from right, it goes down. If beam comes from down, it goes right.
# "\" rotate 90 degree clockwise.
# If beam comes from left, it goes down. If beam comes from down, it goes left.
# if a beam comes from right, it goes up. If beam comes from up, it goes right.
mirrors = {"/": {(0,1): (-1,0), (1,0): (0,-1), (-1,0): [0, 1], (0,-1): ( 1,0)},
          "\\": {(0,1): ( 1,0), (1,0): (0, 1), (-1,0): [0,-1], (0,-1): (-1,0)}}

#splitters split the beam in two beams
# | if beam comes from left or right, it goes up and down
# - if beam comes from up or down, it goes left and right

splitters = {"|": {(1,0): [(1,0)], (-1,0): [(-1,0)], (0,1): [(-1,0), (1,0)], (0,-1): [(-1,0), (1,0)]},
             "-": {(0,1): [(0,1)], (0,-1): [(0,-1)], (1,0): [(0,-1), (0,1)], (-1,0): [(0,-1), (0,1)]}}
#List of beams, each beam has position and direction
beams = []
#Create initial beam with position 0,0 and direction 0,1 (right)
beams.append((0,0,0,1))

def simulate_beam(beam):

    if beam in beam_history:
        return []
    else:
        beam_history.append(_beam)
    #Get position and direction
    y, x, dy, dx = beam
    area = data[y][x]
    new_beams = []
    if area == ".":
        new_beams = [(y+dy, x+dx, dy, dx)]
    if area in mirrors:
        #Get new direction
        new_dy, new_dx = mirrors[area][dy, dx]
        new_beams = [(y+new_dy, x+new_dx, new_dy, new_dx)]
    if area in splitters:
        #Get new directions
        new_ds = splitters[area][dy, dx]
        new_beams = [(y+new_d[0], x+new_d[1], new_d[0], new_d[1]) for new_d in new_ds]
    new_beams = [_beam for _beam in new_beams if 0 <= _beam[0] < len(data) and 0 <= _beam[1] < len(data[0])]
    return new_beams


energy_map = np.zeros((len(data), len(data[0])))
energy_map[0,0] = 1
beam_history = []

while beams:
    _beam = beams.pop(0)
    new_beams = simulate_beam(_beam)
    for _beam in new_beams:
        y, x, _, _ = _beam
        energy_map[y, x] = 1
    beams.extend(new_beams)


print(energy_map)
result = np.sum(energy_map)
print(result)



puzzle.answer_a = result