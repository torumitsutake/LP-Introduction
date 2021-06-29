from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value
from argparse import ArgumentParser


def readfile(problemfile):
    """
    3       //教科数
    5       //一週間の授業日
    6       //時限数
    1,0.5   //最低時限数1,授業重要度1
    1,0.4   //最低時限数2,授業重要度2
    1,0.3   //最低時限数3,授業重要度3
    """
    mintime = list()
    importance = list()
    with open(problemfile, 'r') as f:
        subjectcount = int(f.readline())
        days = int(f.readline())
        times = int(f.readline())
        for _ in range(subjectcount):
            items = f.readline().split(',')
            mintime.append(int(items[0]))
            importance.append(float(items[1]))
    return subjectcount, days, times, mintime, importance


def subjectdecider(subjectcount, days, times, mintime, importance):
    problem = LpProblem(sense=LpMaximize)
    x = []
    for count in range(subjectcount):
        d = []
        for dcount in range(days):
            t = []
            for timecount in range(times):
                t.append(LpVariable('x_'+str(count)+'_'+str(dcount) +
                                    '_'+str(timecount), cat='Binary'))
            d.append(t)
        x.append(d)
    # print(x)
    problem += lpSum(lpSum(lpSum(x[i][d][t]*importance[i] for t in range(times))
                           for d in range(days)) for i in range(subjectcount))
    for i in range(subjectcount):
        problem += lpSum(lpSum(x[i][d][t] for t in range(times))
                         for d in range(days)) >= mintime[i]

    for d in range(days):
        for t in range(times):
            problem += lpSum(x[i][d][t] for i in range(subjectcount)) <= 1
    for d in range(days):
        for i in range(subjectcount):
            problem += lpSum(x[i][d][t] for t in range(times)) <= 2

    solution = problem.solve()
    outlist = [[0 for i in range(days)] for j in range(times)]
    print(outlist)
    print(value(problem.objective))
    for subject in range(subjectcount):
        # print("subject:"+str(subject))
        for day in range(days):
            #print("day:"+str(day)+"   ", end='')
            for time in range(times):
                #print(str(x[subject][day][time].value() * subject)+' ', end="")
                if x[subject][day][time].value() == 1.0:
                    # print(f"day{day}:time{time}:subject{subject}")
                    outlist[time][day] = subject
                    # print(outlist)

            # print('')
    print("       月,火,水,木,金")
    for i in range(len(outlist)):
        print(f"{i}時限目", end='')
        print(outlist[i])


def main(problemfile):
    # minimam,importance,
    # print(problemfile)

    subjectcount, days, times, mintime, importance = readfile(problemfile)
    #print(subjectcount, days, times, mintime, importance)
    subjectdecider(subjectcount, days, times, mintime, importance)


def argparser():
    parser = ArgumentParser()
    parser.add_argument(
        'problem_file',
        help='ClassTime Problem'
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = argparser()
    main(args.problem_file)
