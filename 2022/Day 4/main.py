import re

with open('./Day 4/input.txt') as f:
    lines = f.readlines()

#Parse input

data = [re.findall('\d+', line) for line in lines]
print(data)

 #Check if range is fully contained by another range
def is_contained(a):
    d1 = (int(a[0]),int(a[1]))
    d2 = (int(a[2]),int(a[3]))
    #d1 contains d2
    y_1 = (d1[0] <= d2[0]) and (d1[1] >= d2[1])
    #d2 contains d1
    y_2 = (d2[0] <= d1[0]) and (d2[1] >= d1[1])

    return y_1 or y_2
count = 0
for i in range(len(data)):
        if is_contained(data[i]):
            print(data[i])
            count += 1
print(count)
