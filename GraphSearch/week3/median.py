from heapq import heappush
from heapq import heappop

hmin = []
hmax = []

def hmin_push(i):
    heappush(hmin, -i)

def hmin_pop():
    return -heappop(hmin)

def hmin_peek():
    return -hmin[0]

def hmax_push(i):
    heappush(hmax, i)

def hmax_pop():
    return heappop(hmax)

def hmax_peek():
    return hmax[0]

file = open("Median.txt", "r")

result = 0

for line in file.readlines():
    median = 0
    i = int(line)
    if len(hmin) == 0:
        hmin_push(i)
        median = i
    else:
        if i < hmin_peek():
            hmin_push(i)
        else:
            hmax_push(i)

        if len(hmin) > len(hmax):
            hmax_push(hmin_pop())
        elif len(hmin) < len(hmax):
            hmin_push(hmax_pop())

        if len(hmin) > len(hmax):
            median = hmin_peek()
        elif len(hmin) < len(hmax):
            median = hmax_peek()
        else:
            median = hmin_peek()

    result = (result + median) % 10000


file.close()
print(result)
