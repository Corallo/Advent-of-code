from anytree import Node, RenderTree

# read input
with open('./Day 7/real_input.txt') as f:
    lines = f.readlines()

# create tree
tree = Node('/')
current_dir = tree
tree.data = 0
# parse input
for line in lines:
    if "$ ls" in line:
        continue
    if "dir" in line:
        # extract directory name
        dir_name = line.split(' ')[-1].strip()
        # create a new directory
        node = Node(dir_name, parent=current_dir)
        node.data = 0

    elif "$ cd" in line:
        # extract directory name
        dir_name = line.split(' ')[-1].strip()
        if dir_name == '..':
            # go to parent directory
            current_dir = current_dir.parent
        else:
            # go to directory
            for node in current_dir.children:
                if node.name == dir_name:
                    current_dir = node
                    break
    else:
        # extract file name
        file_name = line.split(' ')[-1].strip()
        file_size = line.split(' ')[-2].strip()
        # add file to current directory
        node = Node(file_name, parent=current_dir)
        node.data = int(file_size)

for pre, fill, node in RenderTree(tree):
    print("%s%s" % (pre, node.name))

def dfs_size(node):
    if len(node.children) == 0:
        return node.data
    size = 0
    #for all children of node
    for child in node.children:
        size += dfs_size(child)
    node.data = size
    return size

# calculate size of each directory recursively
dfs_size(tree)

for pre, fill, node in RenderTree(tree):
    print("%s%s" % (pre, node.name))

# print size of each directory
for node in tree.descendants:
    if len(node.children) == 0:
        continue
    print(node.name, node.data)
print(tree.name, tree.data)

max_size = 70000000
update_size = 30000000
free_space = max_size - tree.data
space_needed = update_size-free_space
print("space needed", space_needed)

# find the smaller directory with size > space_needed
smaller_dir = None
for node in tree.descendants:
    if len(node.children) == 0:
        continue
    if node.data > space_needed:
        if smaller_dir is None:
            smaller_dir = node
        elif node.data < smaller_dir.data:
            smaller_dir = node
print("smaller_dir", smaller_dir.name, smaller_dir.data)