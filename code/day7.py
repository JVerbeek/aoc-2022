class ParentNode():
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.children = []
        self.size = self.get_size()

    def get_size(self):
        return sum([ch.get_size() for ch in self.children])

    def add_children(self, child):
        self.children.append(child)
        return

    def __str__(self):
        return self.name


class ChildNode():
    def __init__(self, name, size, parent) -> None:
        self.name = name
        self.size = size
        self.parent = parent

    def get_size(self):
        return self.size


with open("inputs/day7.txt") as f:
    inp = f.readlines()


nodes = []
current_node = ParentNode("/", None)
nodes.append(current_node)
for line in inp[1:]:
    parts = line.strip().split(" ")
    if parts[1] == "cd":   # Directory
        if parts[2] != "..":
            new_node = ParentNode(parts[2], current_node)
            current_node.add_children(new_node)
            nodes.append(new_node)
            current_node = new_node

        elif parts[2] == "..":
            current_node = current_node.parent
    else:   # File
        try:
            new_node = ChildNode(parts[1], int(parts[0]), current_node)
            current_node.add_children(new_node)
        except ValueError:
            pass

total_space = 70000000
occupied = nodes[0].get_size()
free = total_space - occupied
spacereq = 30000000 - free
candidates = []
for node in nodes:
    size = node.get_size()
    if size >= spacereq:
        candidates.append(size)
print(min(candidates))
        
        
