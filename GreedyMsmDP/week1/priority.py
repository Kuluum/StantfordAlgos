from operator import itemgetter

data = []
with open('jobs.txt', 'r') as file:
    for line in file:
        elems = list(map(lambda e: int(e), line.split()))
        if len(elems) == 2:
            #elems.append(elems[0]-elems[1])
            elems.append(elems[0]*1.0/elems[1])
            data.append(elems)



w_srt_data = sorted(data, key=itemgetter(0), reverse=True)
srt_data = sorted(w_srt_data, key=itemgetter(2), reverse=True)

L = 0
res = 0
for d in srt_data:
    L += d[1]
    res += d[0] * L

print(res)

