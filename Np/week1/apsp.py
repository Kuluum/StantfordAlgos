import sys

with open('g1.txt', 'r') as file:
    meta = file.readline().split()
    V = int(meta[0])
    E = int(meta[1])

    W = [[sys.maxsize for _ in range(V)] for _ in range (V)]    
    for line in file:
        item = list(map(int, line.split()))
        a = item[0]
        b = item[1]
        w = item[2]
        W[a-1][b-1] = w

for k in range(V):
    for i in range(V):
        for j in range(V):
            w = W[i][j]
            wn = W[i][k]+W[k][j]
            W[i][j] = min(w, wn)
    print(k)


has_nc = False
for i in range(V):
    if W[i][i] < 0:
        print("negative cycle!")
        has_nc = True
        break


if not has_nc:
    min_path = W[0][0]
    for i in range(V):
        for j in range(V):
            min_path = min(min_path, W[i][j])
    print(min_path)

