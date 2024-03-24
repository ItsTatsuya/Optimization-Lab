import pulp

def solve_integer_programming(c, A, b):
    problem = pulp.LpProblem("Integer_Programming", pulp.LpMinimize)
    x = [pulp.LpVariable(f'x{i}', lowBound=0, cat=pulp.LpInteger) for i in range(len(c))]
    problem += pulp.lpDot(c, x)
    for i in range(len(A)):
        problem += pulp.lpDot(A[i], x) <= b[i]
    problem.solve()
    solution = [pulp.value(x[i]) for i in range(len(c))]
    optimal_value = pulp.value(problem.objective)
    return optimal_value, solution

def get_input():
    num_variables = int(input("Enter the number of variables: "))
    c = list(map(float, input("Enter the coefficients of the objective function separated by spaces: ").split()))
    A = []
    b = []
    print("Enter the coefficients of the constraint matrix (one row at a time):")
    for _ in range(num_variables):
        row = list(map(float, input().split()))
        A.append(row)
    print("Enter the right-hand side vector (constraints) separated by spaces:")
    b = list(map(float, input().split()))
    return c, A, b

def main():
    c, A, b = get_input()
    optimal_value, solution = solve_integer_programming(c, A, b)
    print("\nOptimal Value:", optimal_value)
    print("Solution:", solution)

if __name__ == '__main__':
    main()
