import random

from sumchef import (
    Equal,
    IsDivisibleBy,
    IsGreaterThan,
    IsLessThan,
    Lit,
    Multiply,
    expression_string,
    find_bindings,
    uniform_domains,
    variables,
)

"""
Prints a list of sums of the form XY0 * Z = ABCD.
"""

var_names = ["x", "y", "z"]
x, y, z = variables(var_names)

lhs = Multiply(x, y)
rhs = z

constraints = [
    IsGreaterThan(x, Lit(50)),
    IsLessThan(x, Lit(1000)),
    IsLessThan(y, Lit(20)),
    IsDivisibleBy(x, Lit(10)),
    Equal(lhs, rhs),
]
domains = uniform_domains(var_names, range(1, 10000))

for b in find_bindings(var_names, domains, constraints, 10):
    hold_out = random.choice([x, y, z])
    lhs_expr = expression_string(lhs, b, hold_out=hold_out)
    rhs_expr = expression_string(rhs, b, hold_out=hold_out)
    print(f"{lhs_expr} = {rhs_expr}")
