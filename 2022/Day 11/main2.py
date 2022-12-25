import re
from tqdm import tqdm
#read input
with open('./Day 11/input.txt') as f:
    line = f.readlines()


class Monkey:
    def __init__(self, id, items, mod,  test_positive, test_negative, adder=0, multiplier=1, square=1):
        self.id = id
        self.items = items
        self.adder = adder
        self.multiplier = multiplier
        self.square = square # Can be 1 or 2
        self.mod = mod
        self.test_positive = test_positive #id of another monkey 
        self.test_negative = test_negative #id of another monkey
        self.operativity = 0

#cread list of monkeys
monkeys = []
#filter lines that have Monkey in them
monkey_lines = [line for line in line if 'Monkey' in line]

#Filter lines that have  Starting items in them
starting_items = [line for line in line if 'Starting items' in line]
#convert multiple digit starting items in ints
starting_items = [line.split(':')[1].strip() for line in starting_items]
#split with ,
starting_items = [line.split(',') for line in starting_items]
#convert to int
starting_items = [[int(x) for x in line] for line in starting_items]

#Filter lines that have  Test in them
test = [line for line in line if 'Test' in line]
#take only the numbers with regex
test = [int(re.findall('\d+', line)[0]) for line in test]

#common denominator test
common_denominator = 1
for item in test:
    common_denominator *= item
print(common_denominator)

#Filter lines "If true:"
if_true = [line for line in line if 'If true:' in line]
#take only the numbers with regex
if_true = [int(re.findall('\d+', line)[0]) for line in if_true]

#Filter lines "If false:"
if_false = [line for line in line if 'If false:' in line]
#take only the numbers with regex
if_false = [int(re.findall('\d+', line)[0]) for line in if_false]

#filter opreation lines
operation_lines = [line for line in line if 'Operation' in line]
#split at =
operation_lines = [line.split('=')[1] for line in operation_lines]
#remove first 3 chars
operation_lines = [line[3:] for line in operation_lines]

adder_list = []
multiplier_list = []
square_list = []
#if opreations contain + 
for operation in operation_lines:
    if '+' in operation:
        adder_list.append( int(operation.split('+')[1]))
        multiplier_list.append(1)
        square_list.append(1)
    elif '*' in operation and 'old' not in operation:
        adder_list.append(0)
        multiplier_list.append(int(operation.split('*')[1]))
        square_list.append(1)
    else:
        adder_list.append(0)
        multiplier_list.append(1)
        square_list.append(2)

print(adder_list)
print(multiplier_list)
print(square_list)

for i in range(len(monkey_lines)):
    monkeys.append(Monkey(i,starting_items[i],test[i],if_true[i],if_false[i],adder_list[i],multiplier_list[i],square_list[i]))



for round in tqdm(range(10000)):
    #print("round ", round)
    for monkey in monkeys:
        #print("Monkey ",monkey.id,":", monkey.items)
        for item in monkey.items:
            monkey.operativity += 1
            item_new = ((item + monkey.adder) * monkey.multiplier ) ** monkey.square
            item_new = item_new % common_denominator

            if (item_new % monkey.mod) == 0:
                monkeys[monkey.test_positive].items.append(item_new)
            else:
                monkeys[monkey.test_negative].items.append(item_new)
        #empty items
        monkey.items = []
        
operativity = []
for monkey in monkeys:
    operativity.append(monkey.operativity)
    print(monkey.id, monkey.operativity)

#multiply the highest and the second highest values of operativity
print(max(operativity) * sorted(operativity)[-2])