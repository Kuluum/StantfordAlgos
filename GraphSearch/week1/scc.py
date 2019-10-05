# Copyright David Bai: Anyone can use this code without permission or referencing the original source
"""
W1 Kosaraju Algorithm
List Based Iterative Implementation to find sizes of strongly connected components
"""

########################################################
# Data Structures

# node labels range from 1 to 875714. 875715 was used because of the range operator... range(875715) goes up to 875714.
num_nodes = 9#875715

# Adjacency representations of the graph and reverse graph
gr = [[] for i in range(num_nodes)]
r_gr = [[] for i in range(num_nodes)]

# The list index represents the node. If node i is unvisited then visited[i] == False and vice versa
visited = [False] * num_nodes

# The list below holds info about sccs. The index is the scc leader and the value is the size of the scc.
scc = [0] * num_nodes

stack = []  # Stack for DFS
order = []  # The finishing orders after the first pass


########################################################
# Importing the graphs
file = open("test_scc.txt", "r") # I named the input file W1_SCC_edges.txt, but you can name it whatever you wish
data = file.readlines()

for line in data:
    items = line.split()
    gr[int(items[0])] += [int(items[1])]
    r_gr[int(items[1])] += [int(items[0])]


########################################################
# DFS on reverse graph

for node in range(num_nodes):
    if node == 0:
        continue

    if not visited[node]:
        stack.append(node)
        visited[node] = True

    while stack:
        done = True
        stack_node = stack[-1]
        for head in r_gr[stack_node]:
            if not visited[head]:
                stack.append(head)
                visited[head] = True
                done = False
        if done:
            stack.pop()
            order.append(stack_node)



########################################################
# DFS on original graph

visited = [False] * len(visited)  # Resetting the visited variable
order.reverse()  # The nodes should be visited in reverse finishing times

for node in order:
    if node == 0:
        continue
    if not visited[node]:
        stack.append(node)
        visited[node] = True
        t = 1
        while stack:
            stack_node = stack.pop()
            for head in gr[stack_node]:
                if not visited[head]:
                    stack.append(head)
                    visited[head] = True
                    t += 1
        scc[node] = t


########################################################
# Getting the five biggest sccs
scc.sort(reverse=True)
print(scc[:5])