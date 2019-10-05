import random
from heapq import heappush, heappop

class Node:
    def __init__ (self, label):
        self.label = label
    def __str__(self):
        return str(self.label)


class UnionFind:
    def __init__(self):
        self.nodes = []

    def make_set(self, node):
        node.parent = node
        self.nodes.append(node)

    def find(self, node):
        if node.parent == node:
            return node
        else:
            return self.find(node.parent)
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        r = random.randint(0, 1)
        if r == 0:
            x_root.parent = y_root
        else:
            y_root.parent = x_root

def status(uf: UnionFind):
    print(' '.join([str(n) for n in uf.nodes]))
    print(' '.join([str(uf.find(n)) for n in uf.nodes]))


heap = []
uf = UnionFind()
clusters_count = 0
with open('clustering1.txt', 'r') as file:
    meta = file.readline().split()
    clusters_count = int(meta[0])
    for i in range(1, clusters_count+1):
        n = Node(i)
        uf.make_set(n)

    for line in file:
        elems = list(map(lambda e: int(e), line.split()))

        if len(elems) == 3:
            x = elems[0]
            y = elems[1]
            rng = elems[2]
            heappush(heap, (rng, x, y))

target_num = 4

while clusters_count != target_num:
    min_edge = heappop(heap)
    x = uf.nodes[min_edge[1]-1]
    y = uf.nodes[min_edge[2]-1]
    if uf.find(x) != uf.find(y):
        uf.union(x, y)
        clusters_count -= 1

space = 0
while space == 0:
    min_edge = heappop(heap)
    x = uf.nodes[min_edge[1]-1]
    y = uf.nodes[min_edge[2]-1]
    xr = uf.find(x)
    yr =  uf.find(y)
    roots = (min(xr.label, yr.label), max(xr.label, yr.label))
    if xr != yr:
        space = min_edge[0]

print(space)


    
