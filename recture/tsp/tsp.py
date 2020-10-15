from collections import namedtuple
from argparse import ArgumentParser

from pulp import LpMaximize, LpProblem, LpVariable, lpSum, lpDot

from tsp_dataset import read_instance_file, TSPInstance


def main(problem_file):
    # read problem file
    tsp_instance = read_instance_file(problem_file)

    # solve problem
    print(tsp_instance.__str__(detail=True))


def knapsack(capacity, items):
    """solve knapsack problem

    Parameters
    ----------
    capacity : int
        capacity of knapsack
    items : list of tuple
        items[i] = ( value of item i, weight of item i)
    """

    prob = LpProblem(sense=LpMaximize)

    x = [ LpVariable(name=f'item{i}', cat='Binary') for i in range(len(items)) ]
    v = [ item.value  for item in items ]
    w = [ item.weight for item in items ]

    prob += lpDot(v, x)
    prob += lpDot(w, x) <= capacity

    prob.solve()


def argparser():
    parser = ArgumentParser()
    parser.add_argument(
        'problem_file',
        help='Knapsack problem file'
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = argparser()
    main(args.problem_file)
