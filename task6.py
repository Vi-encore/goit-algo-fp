items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    selected_items = []
    total_calories = 0
    total_cost = 0

    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']

    return selected_items, total_calories, total_cost

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    item_list = list(items.items())

    for i in range(1, n + 1):
        for j in range(budget + 1):
            if item_list[i-1][1]['cost'] <= j:
                dp[i][j] = max(item_list[i-1][1]['calories'] + dp[i-1][j-item_list[i-1][1]['cost']], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    total_calories = dp[n][budget]
    j = budget
    selected_items = []

    for i in range(n, 0, -1):
        if total_calories <= 0:
            break
        if total_calories == dp[i-1][j]:
            continue
        else:
            selected_items.append(item_list[i-1][0])
            total_calories -= item_list[i-1][1]['calories']
            j -= item_list[i-1][1]['cost']

    total_cost = budget - j
    return selected_items, dp[n][budget], total_cost

# Example usage
budget = 100

selected_items_greedy, total_calories_greedy, total_cost_greedy = greedy_algorithm(items, budget)
print(f"Greedy Algorithm: {selected_items_greedy}, Total Calories: {total_calories_greedy}, Total Cost: {total_cost_greedy}")

selected_items_dp, total_calories_dp, total_cost_dp = dynamic_programming(items, budget)
print(f"Dynamic Programming: {selected_items_dp}, Total Calories: {total_calories_dp}, Total Cost: {total_cost_dp}")