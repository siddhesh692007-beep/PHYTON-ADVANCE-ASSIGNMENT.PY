# 0/1 Knapsack using Top-Down Dynamic Programming
# (Memoization)

def knapsack_top_down(weights, values, n, capacity, memo):

    # Base case
    if n == 0 or capacity == 0:
        return 0

    # Check if result is already calculated
    if memo[n][capacity] != -1:
        return memo[n][capacity]

    # If current item's weight is greater than capacity,
    # we cannot select it
    if weights[n - 1] > capacity:

        memo[n][capacity] = knapsack_top_down(
            weights,
            values,
            n - 1,
            capacity,
            memo
        )

    else:
        # Option 1: Include the item
        include = values[n - 1] + knapsack_top_down(
            weights,
            values,
            n - 1,
            capacity - weights[n - 1],
            memo
        )

        # Option 2: Exclude the item
        exclude = knapsack_top_down(
            weights,
            values,
            n - 1,
            capacity,
            memo
        )

        # Choose the better option
        memo[n][capacity] = max(include, exclude)

    return memo[n][capacity]


# ---------------- Main Program ----------------

weights = [2, 1, 3, 2]
values = [12, 10, 20, 15]

capacity = 5
n = len(weights)

# Create memoization table
memo = [[-1 for _ in range(capacity + 1)]
        for _ in range(n + 1)]

maximum_value = knapsack_top_down(
    weights,
    values,
    n,
    capacity,
    memo
)

print("Maximum value using Top-Down:", maximum_value)
