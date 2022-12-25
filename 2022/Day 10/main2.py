import re

#read file
with open('./Day 10/real_input.txt') as f:
    lines = f.readlines()


# extract signed int from string
data = [re.findall('[-]?\d+', line) for line in lines]
#convert to int
data = [[int(x) for x in line] for line in data]

time_stamp = []
X_list = []
time = 0
X = 1
X_list.append(X)
for line in data:
    if line == []:
        time += 1
        time_stamp.append(time)
        X_list.append(X)
    else:
        time += 1
        time_stamp.append(time)
        X_list.append(X)
        time += 1
        X += line[0]
        time_stamp.append(time)
        X_list.append(X)

print(X_list)

end_time = time_stamp[-1]

drawing = []

print(end_time)
for time in range(end_time):
    
    if (time % 40) == X_list[time] or (time % 40) == X_list[time]-1 or (time % 40) == X_list[time]+1:
        drawing.append("#")
    else:
        drawing.append(".")

print(drawing)
#print drawing in lines by 40
for i in range(0,len(drawing),40):
    print(''.join(drawing[i:i+40]))
