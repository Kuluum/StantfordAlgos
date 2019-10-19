import math

with open('nn.txt', 'r') as file:
    meta = file.readline()
    N = int(meta)

    pos = []    
    for line in file:
        item = list(map(float, line.split()))
        pos.append([item[1], item[2]])

visited = set([0])
curr_pos = 0
curr_dist = 0
MAX = 999999999999999999999

def dist_no_sqrt(i, j):
    return (pos[i][0] - pos[j][0]) ** 2 + (pos[i][1] - pos[j][1]) ** 2

while len(visited) != N:
    min_dist = MAX
    min_next = MAX
    for i in range(N):
        if i in visited:
            continue
        curr_to_i_dist = dist_no_sqrt(curr_pos, i)
        if  curr_to_i_dist < min_dist:
            min_dist = curr_to_i_dist
            min_next = i

    curr_pos = min_next
    curr_dist += math.sqrt(min_dist)
    visited.add(min_next)

    if (len(visited) % 10 == 0):
        print(len(visited)/N)

print("last pos", str(curr_pos))
print("without last hop",  str(curr_dist))

last_hop = math.sqrt(dist_no_sqrt(curr_pos, 0))

print("last hop", str(last_hop))

# back to 0
print("with last hop",  str(curr_dist + last_hop))


