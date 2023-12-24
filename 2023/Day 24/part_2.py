from aocd.models import Puzzle
import numpy as np
from tqdm import tqdm
import sys
import z3
from itertools import combinations
import numpy as np

YEAR = 2023
DAY = 24
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#data = puzzle.examples[0][0]

data = data.splitlines()
data = [line.split("@") for line in data]
data = [[np.array(array.split(","), dtype=np.int64) for array in line] for line in data]



def check_sat(snowflakes):

    t_collision = z3.RealVector('t1', len(snowflakes))
    x_start = z3.Real('x_start')
    y_start = z3.Real('y_start')
    z_start = z3.Real('z_start')
    dx_start = z3.Real('dx_start')
    dy_start = z3.Real('dy_start')
    dz_start = z3.Real('dz_start')
    # check if they collide
    collision_constraints = []
    for i, snowflake in enumerate(snowflakes):
        snowflake_position, snowflake_speed = snowflake

        collision_constraints.append(snowflake_position[0] + snowflake_speed[0] * t_collision[i] == x_start + t_collision[i] * dx_start)
        collision_constraints.append(snowflake_position[1] + snowflake_speed[1] * t_collision[i] == y_start + t_collision[i] * dy_start)
        collision_constraints.append(snowflake_position[2] + snowflake_speed[2] * t_collision[i] == z_start + t_collision[i] * dz_start)
        collision_constraints.append(t_collision[i] >= 0)

    # Create Z3 solver
    s = z3.Solver()

    # Add collision constraints to the solver
    s.add(collision_constraints)

    # Check if the constraints are satisfiable
    if s.check() == z3.sat:
        model = s.model()
        x_start_value = int(model[x_start].as_decimal(10))
        y_start_value = int(model[y_start].as_decimal(10))
        z_start_value = int(model[z_start].as_decimal(10))
        return x_start_value, y_start_value, z_start_value



vars  = check_sat(data)
print(vars)
solution = np.sum(vars)
print(solution)
puzzle.answer_b = solution