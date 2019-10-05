from heapq import heappush, heappop
heap = []
G = []
V = []
with open('edges.txt', 'r') as file:
    meta = file.readline().split()
    G = [[] for _ in range(int(meta[0]) + 1)]
    for line in file:
        elems = list(map(lambda e: int(e), line.split()))
        
        if len(elems) == 3:
            e = G[elems[0]]
            e.append((elems[1], elems[2]))
            G[elems[1]].append((elems[0], elems[2]))

cost = 0
U = set([1])
for e in G[1]:
    heappush(heap, (e[1], e[0]))

while len(U)+1 != len(G) and len(heap) != 0:
    shortest = heappop(heap)
    if shortest[1] in U:
        continue
    U.add(shortest[1])
    cost += shortest[0]
    for e in G[shortest[1]]:
        heappush(heap, (e[1], e[0]))

print(cost)