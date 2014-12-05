#!/usr/bin/env python3

import unittest
import heapq
import sys

# ans is 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068

def dijkstra_shortest_path(vertices, edges, src):
    # Initialize single source:
    vertices[src].d = 0
    # S = 0
    S = {}
    # Q = vertices
    Q = []  # Priority queue
    for vertex in vertices.values():
        heapq.heappush(Q, [vertex.d, vertex.index])
    while Q:
        u = heapq.heappop(Q)
        u_d = u[0]
        u_i = u[1]
        S[u_i] = u_d
        for v, w in edges[u_i]:
            # Relax (u, v, w)
            if vertices[v].d > u_d + w:
                vertices[v].d = u_d + w
                for qind in range(len(Q)):
                    if Q[qind][1] == v:
                        Q[qind][0]= u_d + w
                heapq.heapify(Q)
    return S


class Vertex:
    def __init__(self, index):
        self.index = index
        self.pred = 0
        self.d = 1000000

    def __repr__(self):
        return 'vert: {} {} {}'.format(self.index, self.pred, self.d)

    def __eq__(self, other):
        return self.d == other.d

    def __lt__(self, other):
        return self.d < other.d


def read_graph(file_name):
    edges = {}
    vertices = {}
    with open(file_name) as src_file:
        for line in src_file.readlines():
            line = line.split()
            vert = int(line[0])
            vertices[vert] = Vertex(vert)
            if vert not in edges.keys():
                edges[vert] = set()
            for tup in line[1:]:
                tup = tup.split(',')
                adj_vert = int(tup[0])
                weight = int(tup[1])
                edges[vert].add((adj_vert, weight))
                if adj_vert not in edges.keys():
                    edges[adj_vert] = set()
                edges[adj_vert].add((vert, weight))
    return vertices, edges


class DijkstraTestCase(unittest.TestCase):
    def test_priority_queue(self):
        pass

    def test_dijkstra(self):
        # Basic case
        vertices, edges = read_graph('test_data/test_read.txt')
        path_lengths = dijkstra_shortest_path(vertices, edges, 1)
        assert path_lengths[2] == 10, str(path_lengths)
        assert path_lengths[3] == 30, str(path_lengths)
        # Test01 case
        vertices, edges = read_graph('test_data/test01.txt')
        path_lengths = dijkstra_shortest_path(vertices, edges, 1)
        assert path_lengths == {1: 0, 2: 3, 3: 3, 4: 5}, path_lengths
        # Test02 case
        vertices, edges = read_graph('test_data/test02.txt')
        path_lengths = dijkstra_shortest_path(vertices, edges, 1)
        assert path_lengths == {1: 0, 2: 3, 3: 4, 4: 5}, path_lengths

    def test_read_graph(self):
        vertices, edges = read_graph('test_data/test_read.txt')
        assert vertices == {1: Vertex(1), 2: Vertex(2), 3: Vertex(3)}, vertices
        exp_edges = {1: {(3, 40), (2, 10)}, 2: {(1, 10), (3, 20)}, 3: {(1, 40), (2, 20)}}
        assert edges == exp_edges, edges


if __name__ == '__main__':
    if len(sys.argv) == 1:
        unittest.main()
    else:
        vertices, edges = read_graph('test_data/dijkstraData.txt')
        path_lengths = dijkstra_shortest_path(vertices, edges, 1)
        indices = [7,37,59,82,99,115,133,165,188,197]
        res = ''
        for index in indices:
            res += '{},'.format(path_lengths[index])
        print(res)
