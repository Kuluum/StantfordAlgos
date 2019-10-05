import heapq

num_nodes = 200

V = [[]] * (num_nodes + 1)  # 0  index unused

file = open("dijkstraData.txt", "r")
for line in file.readlines():
    items = line.split()
    v = int(items[0])
    e = [(int(a[0]), int(a[1])) for a in [s.split(',') for s in items[1:]]]
    V[v] = e
file.close()

mins = [1000000 for v in range(num_nodes+1)]
paths = [[] for i in mins]
heap = []
frontier = [False for i in mins]

mins[0] = -1
mins[1] = 0
paths[1] = [1]
# invert in heap: 0 - min length , 1 - node
heapq.heappush(heap, (0, 1))


while heap:

    curr_node = heapq.heappop(heap)
    v = curr_node[1]
    min = curr_node[0]
    if not frontier[v]:
        for next in V[v]:
            next_v = next[0]
            len_to_next = next[1]
            if not frontier[next_v]:
                if min + len_to_next < mins[next_v]:
                    mins[next_v] = min + len_to_next
                    new_path = paths[v].copy()
                    new_path.append(next_v)
                    paths[next_v] = new_path
                    heapq.heappush(heap, (mins[next_v], next[0]))

    frontier[v] = True

target = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
result = [str(mins[i]) for i in target]
print(','.join(result))
