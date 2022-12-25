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
print(time_stamp)

end_time = time_stamp[-1]

sum = 0
for sample in range(20,end_time,40):
    #find time_stamp index
    index = time_stamp.index(sample-1)
    #find X value
    X = X_list[index]
    sum += X*sample
    print(X*sample)
print(sum)

