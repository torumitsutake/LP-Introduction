from math import sqrt
from itertools import combinations, product

import numpy as np


def read_instance_file(tspfile):
    name, dimension, D, C = None, None, None, None

    with open(tspfile, 'r') as f:
        for line in f:
            line = line.strip()
            line = line.replace(':', '')
            if 'NAME' in line:
                name = line.split()[1]
            if 'TYPE' in line:
                pType = line.split()[1]
            if 'DIMENSION' in line:
                dimension = int(line.split()[1])
            if 'EDGE_WEIGHT_TYPE' in line:
                edge_weight_type = line.split()[1]
            if 'EDGE_WEIGHT_FORMAT' in line:
                edge_weight_format = line.split()[1]
            if 'EDGE_WEIGHT_SECTION' in line:
                D = read_edge_weight(
                    f,
                    edge_weight_format,
                    dimension
                )
            if 'NODE_COORD_SECTION' in line:
                N, D = read_node_coord(
                    f,
                    edge_weight_type,
                    dimension,
                    D
                )

    tsp_instance = TSPInstance(name, dimension, D, C)
    return tsp_instance


def read_edge_weight(f, edge_weight_format, dim):
    D = np.zeros((dim, dim))
    if edge_weight_format == 'LOWER_DIAG_ROW':
        i, j = 0, 0
        while i < dim:
            for elm in map(float, f.readline().split()):
                D[i, j] = D[j, i] = elm
                (i, j) = (i, j+1) if j < i else (i+1, 0)
        return D
    if edge_weight_format == 'FULL_MATRIX':
        i, j = 0, 0
        while i < dim:
            for elm in map(float, f.readline().split()):
                D[i, j] = D[j, i] = elm
                j = j + 1
            i, j = i+1, 0
        return D


def read_node_coord(f, edge_weight_type, dim, D):
    N = dict()
    for _ in range(dim):
        line = f.readline()
        node_ix, x, y = line.split()
        node_ix, x, y = int(node_ix), float(x), float(y)
        N[node_ix] = (x, y)
    if edge_weight_type == 'EUC_2D':
        D = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                ii, jj = N[i+1], N[j+1]
                dist = sqrt((ii[0]-jj[0])**2+(ii[1]-jj[1])**2)
                D[i, j] = D[j, i] = dist
    return N, D



class TSPInstance:
    """
    TSP Instance

    Parameters
    ----------
    name : str
      problem name
    dim : int
      dimension (#cities)
    D : numpy array
      Distance matrix (size is dim*dim)
    C : dict
      node coordinate data
    """
    def __init__(self, name, dim, D=None, C=None):
        self.name = name
        self.dim = dim
        self.D = D  # Distance matrix
        self.C = C  # Node Coordinate data


    def __str__(self, detail=False):
        s  = f'NAME: {self.name}\n'
        s += f'DIMENSION: {self.D.shape[0]}'
        if detail:
            s += f'\nD: {self.D}'
        return s
