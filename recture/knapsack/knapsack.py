from argparse import ArgumentParser
from collections import namedtuple

from pulp import LpMaximize, LpProblem, LpVariable, lpSum, lpDot


def main(problem_file):
    # read problem file
    capacity, items = read_problem_file(problem_file)

    # solve problem
    knapsack(capacity, items)


def read_problem_file(problem_file):
    """read knapsack problem file

    Parameters
    ----------
    problem_file : str
        problem file path

    Returns
    -------
    capacity : int
        capacity of knapsack
    items : list of namedtuple
        items[i].value, value of item i
        items[i].weight, weight of item i
    """
    capacity = None
    items = list()

    Item = namedtuple('Item', ('value', 'weight'))
    with open(problem_file, 'r') as f:
        n = int(f.readline())
        capacity = int(f.readline())
        for _ in range(n):
            value, weight = map(int, f.readline().split())
            items.append(Item(value=value, weight=weight))

    return capacity, items


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
    #変数定義
    x = []
    n = len(items)
    #x = LpVariable.dicts('x',range(n),cat='Binary')
    #print(x)
    for count in range(n):
        x.append(LpVariable('x'+str(count),cat='Binary'))
    #目的関数
    prob += lpSum((items[i].value * x[i]) for i in range(n))
    #制約条件
    prob += lpSum((items[i].weight * x[i]) for i in range(n)) <= capacity

    solution = prob.solve()
    #for i in range(n):
        #print(int(x[i].value()))

    ...



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
