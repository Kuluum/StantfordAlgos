
edges = [0]

A = []
used = []

with open('mwis.txt', 'r') as file:
    meta = file.readline()
    A = [0 for _ in range(int(meta)+1)]
    used = [[] for _ in range(int(meta)+1)]
    for line in file:
        edges.append(int(line))

A[1] = edges[1]
used[1] = [1]
for i in range(2, len(A)):
    if A[i-1] > A[i-2] + edges[i]:
        A[i] = A[i-1]
        used[i] = used[i-1]
    else:
        A[i] =  A[i-2] + edges[i]
        used[i] = used[i-2] + [i]

print(A[-1])
print(used[-1])

check = [1, 2, 3, 4, 17, 117, 517, 997]

result = [1 if c in used[-1] else 0 for c in check]
print(''.join(map(str, result)))