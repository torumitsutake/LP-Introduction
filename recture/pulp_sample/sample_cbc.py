from pulp import LpVariable, LpProblem, value

x = LpVariable('x')
y = LpVariable('y', lowBound=-3)

prob = LpProblem()
prob += -x + 4*y
prob += -3*x + y <= 6
prob += -x - 2*y >= -4

prob.solve()

print(value(prob.objective), value(x), value(y))
