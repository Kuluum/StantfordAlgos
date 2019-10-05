
with open('knapsack1.txt', 'r') as file:
    meta = file.readline().split()
    W = int(meta[0])
    N = int(meta[1])
    A = [[0]*(W+1) for _ in range(2)]
    I = []
    for line in file:
        item = list(map(int, line.split()))
        I.append(item)

for i in range(1, N+1):
    for x in range(W+1):
        a1 = A[0][x]
        vi = I[i-1][0]
        wi = I[i-1][1]
        if (x>=wi):
            a2 = A[0][x-wi]+vi
        else:
            a2 = 0
        A[1][x] = max(a1, a2)
    A[0] = A[1]
    A[1] = [0 for _ in range(W+1)]
    print(i)

print(A[0][W])

#4243395