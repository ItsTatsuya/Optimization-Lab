import numpy as np

def transportation_northwest(c, A, b):
    m, n = A.shape
    supply = np.sum(A, axis=1)
    demand = np.sum(A, axis=0)
    if not np.array_equal(supply, b) or not np.array_equal(demand, c):
        raise ValueError("Supply and demand constraints are not balanced.")
    
    # Initialize variables
    x = np.zeros((m, n))
    i, j = 0, 0
    
    # Start from the northwest corner and allocate until the supply or demand is exhausted
    while i < m and j < n:
        if supply[i] < demand[j]:
            x[i][j] = supply[i]
            demand[j] -= supply[i]
            supply[i] = 0
            i += 1
        else:
            x[i][j] = demand[j]
            supply[i] -= demand[j]
            demand[j] = 0
            j += 1
    
    return x

def transportation_least_cost(c, A, b):
    m, n = A.shape
    supply = np.sum(A, axis=1)
    demand = np.sum(A, axis=0)
    if not np.array_equal(supply, b) or not np.array_equal(demand, c):
        raise ValueError("Supply and demand constraints are not balanced.")
    
    # Initialize variables
    x = np.zeros((m, n))
    cost = A * c.reshape(1, -1)
    
    while np.sum(x) < m * n:
        min_cost_index = np.unravel_index(np.argmin(cost), cost.shape)
        i, j = min_cost_index
        min_supply_demand = min(supply[i], demand[j])
        x[i][j] = min_supply_demand
        supply[i] -= min_supply_demand
        demand[j] -= min_supply_demand
        cost[i][j] = np.inf  # Mark as visited
    
    return x

def transportation_vam(c, A, b):
    m, n = A.shape
    supply = np.sum(A, axis=1)
    demand = np.sum(A, axis=0)
    if not np.array_equal(supply, b) or not np.array_equal(demand, c):
        raise ValueError("Supply and demand constraints are not balanced.")
    
    # Initialize variables
    x = np.zeros((m, n))
    cost = A * c.reshape(1, -1)
    
    while np.sum(x) < m * n:
        # Calculate the penalties for rows and columns
        row_penalties = np.zeros(m)
        col_penalties = np.zeros(n)
        for i in range(m):
            row_values = np.sort(cost[i][cost[i] > 0])
            if len(row_values) > 1:
                row_penalties[i] = row_values[1] - row_values[0]
        for j in range(n):
            col_values = np.sort(cost[:, j][cost[:, j] > 0])
            if len(col_values) > 1:
                col_penalties[j] = col_values[1] - col_values[0]
        
        max_row_penalty_index = np.argmax(row_penalties)
        max_col_penalty_index = np.argmax(col_penalties)
        
        if row_penalties[max_row_penalty_index] > col_penalties[max_col_penalty_index]:
            i = max_row_penalty_index
            j = np.argmin(cost[i])
        else:
            j = max_col_penalty_index
            i = np.argmin(cost[:, j])
        
        min_supply_demand = min(supply[i], demand[j])
        x[i][j] = min_supply_demand
        supply[i] -= min_supply_demand
        demand[j] -= min_supply_demand
        cost[i][j] = np.inf  # Mark as visited
    
    return x

def main():
    c = [3, 2, 7]
    A = np.array([[2, 5, 2], [4, 1, 3], [3, 6, 4]])
    b = [10, 20, 15]
    
    # Northwest Corner Method
    print("Northwest Corner Method:")
    x_nw = transportation_northwest(c, A, b)
    print(x_nw)
    
    # Least Cost Method
    print("\nLeast Cost Method:")
    x_lc = transportation_least_cost(c, A, b)
    print(x_lc)
    
    # Vogel's Approximation Method
    print("\nVogel's Approximation Method:")
    x_vam = transportation_vam(c, A, b)
    print(x_vam)

if __name__ == '__main__':
    main()
