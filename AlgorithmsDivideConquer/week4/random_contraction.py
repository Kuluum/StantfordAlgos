from random import randint

graph = {}
with open('kargerMinCut.txt', 'r') as file:
    for line in file:
        splitted = line.split()
        v = splitted[0]
        e = splitted[1:]
        graph[v] = e


# graph = {
#     1: [2, 3],
#     2: [1, 3, 4],
#     3: [1, 2, 4],
#     4: [2, 3]
# }

def randContr(graph):
    while len(graph.keys()) > 2:
        keys = list(graph.keys())
        v_ind = randint(0, len(keys)-1)
        v = keys[v_ind]
        e = graph[v]
        v2_ind = randint(0, len(e)-1)
        v2 = e[v2_ind]

        e2 = graph[v2]
        #print('merge ' + str(v) + ' ' + str(v2))
        new_e = e + e2
        new_e = list(filter(lambda a: (a != v and a != v2), new_e))
        graph[v] = new_e
        for e_v in new_e:
            graph[e_v] = list(map(lambda a: v if a == v2 else a, graph[e_v]))
        del graph[v2]
    return graph

g = randContr(graph)

new_k = list(g.keys())
c0 = len(g[new_k[0]])
c1 = len(g[new_k[1]])

print(c0, c1)