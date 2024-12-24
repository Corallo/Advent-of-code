#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle


DAY=17
session_id = open("Session", "r").read()
data = get_data(day=DAY, year=2024,session=session_id)

"""with open(f'2024/day {DAY}/data.txt', 'r') as file:
    data = file.read()
"""

program = [2,4,
           1,2,
           7,5,
           4,1,
           1,3,
           5,5,
           0,3,
           3,0]

def simulate_code(A):
    out=  []
    while A!=0:
        x = A % 8
        y = x ^ 2
        z = (y ^ (A // (2**y)) ^ 3) % 8
        out.append(z)
        A = A // 8
    return out


def recursive_sol(A):
    out = simulate_code(A)
    if  out != program[-len(out):]:
        return

    print(A, out)

    if len(out) == len(program):
        print("Found a solution:", A)
        exit()

    for j in range(8):
        recursive_sol((A << 3) + j)

for x in range(8):
    recursive_sol(x)




#submit(out_str, part="a", day=DAY, year=2024, session=session_id)