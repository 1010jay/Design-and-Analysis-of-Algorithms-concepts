# Supply Chain Cost Minimization using Dynamic Programming

def minimize_supply_chain_cost(cost_matrix):
    num_warehouses = len(cost_matrix)
    num_suppliers = len(cost_matrix[0])
    
    # DP table to store minimum costs
    dp = [[float('inf')] * num_suppliers for _ in range(num_warehouses)]
    # To track the supplier chosen for each warehouse
    track_supplier = [[-1] * num_suppliers for _ in range(num_warehouses)]

    # Initialize the first warehouse costs
    for j in range(num_suppliers):
        dp[0][j] = cost_matrix[0][j]

    # Fill the DP table
    for i in range(1, num_warehouses):
        for j in range(num_suppliers):
            for k in range(num_suppliers):
                if dp[i][j] > dp[i - 1][k] + cost_matrix[i][j]:
                    dp[i][j] = dp[i - 1][k] + cost_matrix[i][j]
                    track_supplier[i][j] = k

    # Find the minimum cost in the last row
    min_cost = float('inf')
    last_supplier = -1
    for j in range(num_suppliers):
        if dp[-1][j] < min_cost:
            min_cost = dp[-1][j]
            last_supplier = j

    # Reconstruct the supplier path
    supplier_path = []
    current_supplier = last_supplier
    for i in range(num_warehouses - 1, -1, -1):
        supplier_path.append(current_supplier)
        current_supplier = track_supplier[i][current_supplier]

    supplier_path.reverse()
    return min_cost, supplier_path


# Example cost matrix (rows: warehouses, columns: suppliers)
cost_matrix = [
    [4, 6, 8],
    [2, 5, 7],
    [3, 4, 6],
]

min_cost, supplier_path = minimize_supply_chain_cost(cost_matrix)

print("Minimum Supply Chain Cost:", min_cost)
print("Optimal Supplier Configuration:", supplier_path)