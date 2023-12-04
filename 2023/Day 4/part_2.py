from aocd.models import Puzzle

YEAR = 2023
DAY = 4
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#data = puzzle.examples[0][0]
print(data)

data = data.split("\n")
#Remove everything before ":"
data = [x.split(": ")[1] for x in data]
data = [x.split(" | ") for x in data]
data = [[x.split(" ") for x in y] for y in data]
#Remove empty strings
data = [[[z for z in y if z != ""] for y in x] for x in data]
#Convert to int
data = [[[int(z) for z in y] for y in x] for x in data]
print(data)

score = 0
cards = [1]*len(data)
for idx, game in enumerate(data):
    my_cards = game[1]
    winning_cards = game[0]
    points = len(set(my_cards) & set(winning_cards))
    for i in range(points):
        cards[idx+i+1] += 1*cards[idx]

score = sum(cards)



puzzle.answer_b = score