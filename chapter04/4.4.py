def topological_sort(graph):
    inDeg = {}
    for V in graph:
        inDeg[V] = 0
    for V in graph:
        for u in graph[V]:
            inDeg[u] += 1

    vlist = []
    for v in graph:
        if inDeg[v] == 0:
            vlist.append(v)

    while vlist:
        v = vlist.pop()
        print(v, end=' ')

        for u in graph[v]:
            inDeg[u] -= 1
            if inDeg[u] == 0:
                vlist.append(u)

mygraph = {
    "A": {"C", "D"},
    "B": {"D", "F"},
    "C": {"D", "F"},
    "D": {"F"},
    "E": {"F"},
    "F": {}
}
print('위상 정렬 결과: ')
topological_sort(mygraph)
print()
