from pulp import LpVariable, LpProblem, value
from pulp import GLPK_CMD

x = LpVariable('x')
y = LpVariable('y', lowBound=-3)

prob = LpProblem()
prob += -x + 4*y
prob += -3*x + y <= 6
prob += -x - 2*y >= -4

solver = GLPK_CMD(
        # path="/home/tateiwa/pulp_rec/solvers/usr/bin/glpsol",
        msg=True
        )
prob.solve(solver=solver)

print(value(prob.objective), value(x), value(y))
