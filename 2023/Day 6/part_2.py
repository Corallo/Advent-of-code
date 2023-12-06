from aocd.models import Puzzle

YEAR = 2023
DAY = 6
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#data = puzzle.examples[0][0]
print(data)
data = data.split("\n")

times = data[0].split(": ")[1].replace(" ", "")
distances = data[1].split(": ")[1].replace(" ", "")
time = int(times)
distance = int(distances)

print(time)
print(distance)

score = 1

victory_counter = 0
for v in range(1, time):
    if (v*(time-v) > distance):
        victory_counter += 1
score *= victory_counter

print(score)
puzzle.answer_b= score