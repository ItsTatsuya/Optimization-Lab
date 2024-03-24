import numpy as np
from scipy.optimize import linear_sum_assignment

def assignment_problem(cost_matrix):
    cost_matrix = np.array(cost_matrix)
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    min_cost = cost_matrix[row_ind, col_ind].sum()
    assignment = list(zip(row_ind, col_ind))
    return min_cost, assignment

def get_cost_matrix():
    rows = int(input("Enter the number of rows in the cost matrix: "))
    cols = int(input("Enter the number of columns in the cost matrix: "))
    cost_matrix = []
    print("Enter the cost matrix values (separated by spaces):")
    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print("Error: Invalid number of columns.")
            return None
        cost_matrix.append(row)
    return cost_matrix

def main():
    cost_matrix = get_cost_matrix()
    if cost_matrix is None:
        return
    min_cost, assignment = assignment_problem(cost_matrix)
    print("\nMinimum Cost:", min_cost)
    print("Assignment:", assignment)

if __name__ == '__main__':
    main()
