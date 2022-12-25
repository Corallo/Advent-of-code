#read file
with open("Day 25/input.txt") as f:
        data = f.readlines()

data = [line.strip() for line in data]

#convert - in -1 and = in -2
data = [[-1 if char == "-" else -2 if char == "=" else int(char) for char in line] for line in data]
#convert in int
data = [[int(char) for char in line] for line in data]


print(data)

def baseSNAFU_to_base10(base5):
    base10 = 0
    for i, digit in enumerate(reversed(base5)):
        base10 += digit * (5 ** i)
    return base10

print(sum([baseSNAFU_to_base10(line) for line in data]))

def base10_to_baseSNAFU(base10):
    baseSNAFU = ""
    rest = 0
    while base10 != 0 or rest:
        div = base10 % 5 + rest
        rest = int(div > 2)
        baseSNAFU = {0: "0", 1: "1", 2: "2", 3: "=", 4: "-", 5: "0"}[div] + baseSNAFU
        base10 //= 5
    return baseSNAFU

print(base10_to_baseSNAFU(sum([baseSNAFU_to_base10(line) for line in data])))

