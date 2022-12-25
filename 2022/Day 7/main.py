#Read file
with open('./Day 7/input.txt') as f:
    lines = f.readlines()


#parse input, generate a directory tree
tree = {}
tree['/']= {}
for line in lines:
    # if line contains "ls"
    if "dir" in line:
        #extract directory name
        dir_name = line.split(' ')[-1].strip()
        #create a new directory
        tree[dir_name] = {}
    elif "cd" in line:
        #extract directory name
        dir_name = line.split(' ')[-1].strip()
        if dir_name == '..':
            #go to parent directory
            tree = tree['/']
        #go to directory
        tree = tree[dir_name]

    else:
        #extract file name
        file_name = line.split(' ')[-1].strip()
        file_size = line.split(' ')[-2].strip()
        #add file to current directory
        tree[file_name] = file_size

print(tree)


    