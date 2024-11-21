import numpy as np

def inventory_management(dp_horizon, initial_inventory, demand, holding_cost, shortage_cost, reorder_cost, max_inventory):
    # Define the number of periods
    periods = len(dp_horizon)
    
    # Initialize cost table
    dp = np.full((periods + 1, max_inventory + 1), float('inf'))
    dp[periods, :] = np.arange(max_inventory + 1) * holding_cost  # Final holding cost

    # Backward dynamic programming
    for t in range(periods - 1, -1, -1):
        for s in range(max_inventory + 1):  # Inventory level at start of period
            for q in range(max_inventory - s + 1):  # Reorder quantity
                # Calculate next state and costs
                next_inventory = s + q - demand[t]
                holding = holding_cost * max(0, next_inventory)
                shortage = shortage_cost * max(0, -next_inventory)
                order_cost = reorder_cost if q > 0 else 0
                next_cost = dp[t + 1, max(0, min(next_inventory, max_inventory))]

                dp[t, s] = min(dp[t, s], order_cost + holding + shortage + next_cost)

    # Reconstruct optimal reorder policy
    policy = []
    current_inventory = initial_inventory
    for t in range(periods):
        best_q = 0
        min_cost = float('inf')
        for q in range(max_inventory - current_inventory + 1):
            next_inventory = current_inventory + q - demand[t]
            holding = holding_cost * max(0, next_inventory)
            shortage = shortage_cost * max(0, -next_inventory)
            order_cost = reorder_cost if q > 0 else 0
            next_cost = dp[t + 1, max(0, min(next_inventory, max_inventory))]
            total_cost = order_cost + holding + shortage + next_cost

            if total_cost < min_cost:
                min_cost = total_cost
                best_q = q

        policy.append(best_q)
        current_inventory += best_q - demand[t]

    return dp[0, initial_inventory], policy

# Example Usage
dp_horizon = [1, 2, 3, 4, 5]  # Time periods
initial_inventory = 10
demand = [5, 7, 3, 9, 6]  # Forecasted demand
holding_cost = 2
shortage_cost = 5
reorder_cost = 50
max_inventory = 20

optimal_cost, reorder_policy = inventory_management(dp_horizon, initial_inventory, demand, holding_cost, shortage_cost, reorder_cost, max_inventory)
print(f"Optimal Cost: {optimal_cost}")
print(f"Reorder Policy: {reorder_policy}")
