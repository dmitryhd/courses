#!/usr/bin/python
#-*- coding: utf-8 -*-

def load_data(filename):
    edges = []
    with fd = open(filename):
        fd.readline()
        for line in fd.readlines():
            sline = line.split()
            edges.append(int(sline[0]), int(sline[1]))
    return edges



    graph = {}
    for val in v:
        graph[val] = [[],False]
    for edge in edges:
        graph[edge[0]][0].append(edge[1])

    def dfs(graph, start):
        S = [start]
        while S:
            v = S.pop()
            if graph[v][1] == False:
                graph[v][1] = True
                for w in graph[v][0]:
                    S.append(w)

    def find_connected_components(graph):
        res = 0
        all_visited = False
        while not all_visited:
            for v in graph.keys():
                if graph[v][1] == False:
                    dfs(graph, v)
                    res += 1
            all_visited = True
            for v in graph.keys():
                if graph[v][1] == False:
                    all_visited = False
        return res
