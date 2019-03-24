#!/usr/bin/env python
# encoding:UTF-8

import numpy as np
import gc
import pickle


def sort_two_vertices(a, b):
    if a > b:
        return b, a
    return a, b


def read_edge_list(filename, delimiter=None, nodetype=int):
    """Generate the adjacent matrix of a graph with overlapping communities.
       Input: A two-clumn edgelist
       Return: An adjacency matrix in the form of ndarray corresponding to the given edge list.
    """
    edgeset = set()
    nodeset = set()

    node_number = 1791489
    graph_linklist = [set() for i in range(0, node_number)]  # Initialize the graph in the format of linked list
    for i in range(node_number):
        graph_linklist[i].add(i)

    print "Reading the edgelist..."
    with open(filename, 'U') as f:
        for line in f.readlines():
            if not line.strip().startswith("#"):
                L = line.strip().split(delimiter)
                ni, nj = nodetype(L[0])+1, nodetype(L[1])+1
                nodeset.add(ni)
                nodeset.add(nj)
                if ni != nj:
                    edgeset.add(sort_two_vertices(ni, nj))
                    a = ni - 1
                    b = nj - 1
                    graph_linklist[a].add(b)
                    graph_linklist[b].add(a)
        node_number = len(list(nodeset))
        edge_number = len(list(edgeset))
    del edgeset

    print "The network has", node_number, "nodes with", edge_number, "edges."

    del nodeset

    gc.collect()

    degree = []
    for node in range(node_number):
        degree.append(len(graph_linklist[node]))

    print "Finish constructing graph."
    print "-------------------------------------------------------"

    return graph_linklist, node_number, edge_number, degree


def read_ground_truth(filename, delimiter=None, nodetype=int):
    print "Parsing ground truth communities..."
    communities = []

    with open(filename, 'U') as f:
        count = 0
        for line in f.readlines():
            if not line.strip().startswith("#"):
                L = line.strip().split('\t')
                membership_array = np.fromstring(L[0], dtype=int, sep=' ')

                communities.append(membership_array)
    print "Finish parsing communities."
    return communities, len(communities)


def read_cat(filename, comunity):
    cat_dict = {}
    for node in range(1791489):
        cat_dict[node] = []

    with open(filename, 'U') as f:
        for line in f.readlines():
            if not line.strip().startswith("#"):
                L = line.strip().split(';')
                cat = L[0][9:]
                nodes = L[1].strip().split(" ")
                for node in nodes:
                    if node == '':
                        continue
                    cat_dict[int(node)].append(cat)


    res = {}
    for node in comunity:
        cats = cat_dict[node]
        for cat in cats:
            if cat not in res:
                res[cat] = [node]
            else:
                res[cat].append(node)

    for key, value in res.items():
        print(key, value)

if __name__ == "__main__":
    comunity = [1017534, 497561, 1731663, 1357106, 1372183, 1389573, 734185, 715589, 1017539, 1017540, 1017559, 1017535, 1017533, 1017662, 1017525, 1017542, 1017555, 1017560, 1017529, 1017546, 1742642, 1017723, 1030871, 1655801, 1017614, 1015791, 465338, 1017541, 1017543, 1071982, 698256, 1016355, 724498, 1017463, 1017536, 393953, 1083795, 1017508, 362516, 1017627, 279121, 1655581, 1017617, 340291, 394840, 1056192, 1017553, 1016341, 1017554, 456261, 1060112, 1016350, 1017615, 1017619, 1017475, 1017616, 1017724, 1016351, 1017618, 1018485, 1017720, 186607, 1016348, 1017565, 1017545, 1017443, 1017496, 1163043, 1017725, 1017531, 395990, 1016114, 1017522, 1017563, 1017550, 1017823, 592938, 1017544, 1060115, 1016345, 592939, 1017625, 1016360, 1429128, 1017969, 1017719, 576379, 1016053, 1016343, 1018302, 1017564, 1017562, 1017474, 1017527, 1017526, 490901]
    read_cat("../example/wiki/wiki-topcats-categories.txt", comunity)
