#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle

DAY=22
session_id = open("Session", "r").read()
data = get_data(day=DAY, year=2024,session=session_id)


"""with open(f'2024/day {DAY}/data.txt', 'r') as file:
    data = file.read()"""

data = data.split("\n")

print(data)

def generate_secret_number(n, iteration):
    for _ in range(iteration):
        n = ((n * 64) ^ n ) % 16777216
        n = ((n//32) ^ n ) % 16777216
        n = ((n * 2048) ^ n ) % 16777216
    #print(n)
    return n

answer = sum(generate_secret_number(int(d), 2000) for d in data)

print(answer)
submit(answer, part="a", day=DAY, year=2024, session=session_id)