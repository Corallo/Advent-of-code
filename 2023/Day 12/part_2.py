from aocd.models import Puzzle
import numpy as np
from tqdm import tqdm
from functools import cache
YEAR = 2023
DAY = 12
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#with open("Day 12/data.txt", "r") as f:
#    data = f.read()
print(data)

data = data.split("\n")


@cache
def find_solution(solution, checksum, tmp_counter):

    if solution == "" and len(checksum) == 0 and tmp_counter == 0:
        return 1
    if solution == "":
        return 0

    sol_counter = 0
    # If we reach a ".", we can either continue, or verify that the checksum is correct
    if solution[0] == ".":
        if tmp_counter != 0:
            if len(checksum) != 0 and checksum[0] == tmp_counter:
                # continue with next checksum
                sol_counter += find_solution(solution[1:], checksum[1:], 0)
        else:
            # . found but not counting any #, just go on
            sol_counter += find_solution(solution[1:], checksum, 0)
    # if we reach a # we count it
    elif solution [0] == "#":
        sol_counter += find_solution(solution[1:], checksum, tmp_counter+1)

    # Case for ?, we do first the # case and then the . case
    elif solution[0] == "?":
        # simulate #
        sol_counter += find_solution(solution[1:], checksum, tmp_counter+1)
        if tmp_counter != 0:
            # simulate .
            if len(checksum) != 0 and checksum[0] == tmp_counter:
                sol_counter += find_solution(solution[1:], checksum[1:], 0)
        else:
            sol_counter += find_solution(solution[1:], checksum, 0)
    return sol_counter



result = 0
for line in tqdm(data):
    line = line.split(" ")
    solution = line[0]
    solution = "?".join([solution]*5)
    checksum = line[1]
    checksum = ",".join(checksum.split(",")*5)
    #convert to tuple of ints
    checksum = tuple(map(int,checksum.split(",")))
    counter = find_solution(solution+".", checksum,0)
    #print(counter)
    result += counter

puzzle.answer_b = result