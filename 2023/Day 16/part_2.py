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

#@cache
def simulate_beam(beam,beam_history):
    if beam in beam_history:
        return []
    else:
        beam_history.append(beam)
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




def simulate(initial_beam):
    beams = [initial_beam]
    energy_map = np.zeros((len(data), len(data[0])))
    energy_map[initial_beam[0],initial_beam[1]] = 1
    beam_history = []
    while beams:
        _beam = beams.pop(0)
        new_beams = simulate_beam(_beam, beam_history)
        for _beam in new_beams:
            y, x, _, _ = _beam
            energy_map[y, x] = 1
        beams.extend(new_beams)
    return np.sum(energy_map)


possible_starting_points = []

#add to start point all possible beams from the top going down
for x in range(len(data[0])):
    possible_starting_points.append((0,x,1,0))
#add to start point all possible beams from the bottom going up
for x in range(len(data[0])):
    possible_starting_points.append((len(data)-1,x,-1,0))
#add to start point all possible beams from the left going right
for y in range(len(data)):
    possible_starting_points.append((y,0,0,1))
#add to start point all possible beams from the right going left
for y in range(len(data)):
    possible_starting_points.append((y,len(data[0])-1,0,-1))


max_energy = 0
for start in tqdm(possible_starting_points):
    solution = simulate(start)
    if solution > max_energy:
        max_energy = solution
        print("Found new best start:", start, "with energy:", solution)

print(max_energy)
puzzle.answer_b = max_energy