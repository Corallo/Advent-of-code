from aocd.models import Puzzle
import numpy as np
YEAR = 2023
DAY = 12
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#with open("Day 12/data.txt", "r") as f:
#    data = f.read()

data = data.split("\n")

def check_valid_solution(solution, checksum):

    solution = "".join(solution)
    #print(solution)
    solution = solution.split(".")
    solution = [x for x in solution if x != ""]

    checksum = checksum.split(",")
    checksum = [int(x) for x in checksum]
    if len(solution) != len(checksum):
        return False
    for i in range(len(solution)):
        if len(solution[i]) != checksum[i]:
            return False
    return True

def find_solution(solution, checksum,counter,index):
    #count number of "?" in solution, one line
    if solution.count("?") == 0:
        counter[0] += check_valid_solution(solution, checksum)
    else:
        if index < len(solution):
            if solution[index] == "?":
                new_solution = solution.copy()
                new_solution[index] = "."
                find_solution(new_solution, checksum,counter, index+1)
                new_solution[index] = "#"
                find_solution(new_solution, checksum,counter, index+1)
            else:
                find_solution(solution, checksum,counter, index+1)


result = 0
for line in data:
    line = line.split(" ")
    solution = line[0]
    checksum = line[1]
    counter = [0]
    find_solution(list(solution), checksum, counter,0)
    print(counter[0])
    result += counter[0]


print("Final solution:", result)
puzzle.answer_a = result