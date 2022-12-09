# first star
class Node:
    def __init__(self, name, parent, is_dir=False, size=None):
        self.name = name
        self.parent = parent
        self.children = {}
        self.is_dir = is_dir
        self.size = size

    def insert(self, node):
        assert self.is_dir
        self.children[node.name] = node

with open("input/logs.txt") as f:
    logs = [line.strip() for line in list(f)]

root = Node("/", parent=None, is_dir=True)
pos = root

for log in logs:
    tokens = log.split(" ")
    if tokens[0] == "$":
        if tokens[1] == "cd":
            if tokens[2] == "/":
                pos = root
            elif tokens[2] == "..":
                pos = pos.parent
            else:
                if tokens[2] not in pos.children:
                    pos.insert(Node(tokens[2], parent=pos, is_dir=True))
                pos = pos.children[tokens[2]]
        elif tokens[1] == "ls":
            pass
    elif tokens[0] == "dir":  # dir
        pos.insert(Node(tokens[1], parent=pos, is_dir=True))
    elif tokens[0].isnumeric():  # file
        pos.insert(Node(tokens[1], parent=pos, size=int(tokens[0])))

def tree(node, depth=0):  # print tree of current pos
    if node.is_dir:
        print(f"{' ' * depth * 2}- {node.name} (dir)")
        for child in node.children.values():
            tree(child, depth=depth+1)
    else:
        print(f"{' ' * depth * 2}- {node.name} (file, size={node.size})")

tree(root)

def size(node, sizes):
    assert node.is_dir
    total = 0
    for child in node.children.values():
        if child.is_dir:
            total += size(child, sizes)
        else:
            total += child.size

    sizes.append(total)

    return total

sizes = []
root_size = size(root, sizes)

print(sum([s for s in sizes if s <= 100000]))

# second star
total_space = 70000000
required_space = 30000000
available_space = total_space - root_size
to_free_space = required_space - available_space

print(sorted([s for s in sizes if s >= to_free_space])[0])