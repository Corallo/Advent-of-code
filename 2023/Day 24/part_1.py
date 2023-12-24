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

pairs = list(combinations(data, 2))


def check_sat(_pair):
    test_area = [200000000000000, 400000000000000]
    snowflake_1, snowflake_2 = _pair
    snowflake_position_1, snowflate_speed_1 = snowflake_1
    snowflake_position_2, snowflate_speed_2 = snowflake_2

    x1, y1, t1 = z3.Reals("x1 y1 t1")
    x2, y2, t2 = z3.Reals("x2 y2 t2")

    # check if they collide
    collision = z3.And(x1 == x2, # They meed
                       y1 == y2,

                       x1 >= test_area[0], # In the test area
                       x1 <= test_area[1],
                       y1 >= test_area[0],
                       y1 <= test_area[1],

                       t1 >= 0, # In the future
                       t2 >= 0
                       )
    movement_1 = z3.And(x1 == snowflake_position_1[0] + t1 * snowflate_speed_1[0],
                        y1 == snowflake_position_1[1] + t1 * snowflate_speed_1[1])
    movement_2 = z3.And(x2 == snowflake_position_2[0] + t2 * snowflate_speed_2[0],
                        y2 == snowflake_position_2[1] + t2 * snowflate_speed_2[1])

    # solve
    s = z3.Solver()
    s.add(collision)
    s.add(movement_1)
    s.add(movement_2)
    return s.check() == z3.sat


results = list(tqdm(map(check_sat, pairs), total=len(pairs)))
solution = np.sum(results)
puzzle.answer_a = solution