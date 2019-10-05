from heapq import heappush, heappop

class Node:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.left = None
        self.right = None
        self.min_len = 0
        self.max_len = 0

    def __lt__(self, other):
        return self.weight < other.weight

heap = []


with open('huffman.txt', 'r') as file:
    meta = file.readline().split()
    #elem_count = int(meta[0])
    value = 0
    for line in file:
        weight = int(line)
        n = Node(value, weight)
        heappush(heap, (weight, n))
        value += 1

while len(heap) > 1:
    min1 = heappop(heap)[1]
    min2 = heappop(heap)[1]
    meta_node = Node((min1.value, min2.value), min1.weight + min2.weight)
    meta_node.left = min1
    meta_node.right = min2
    meta_node.min_len = min(min1.min_len, min2.min_len) + 1
    meta_node.max_len = max(min1.max_len, min2.max_len) + 1
    heappush(heap, (meta_node.weight, meta_node))

root = heappop(heap)[1]
print(root.min_len)
print(root.max_len)