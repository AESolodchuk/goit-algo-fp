items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    total_calories = 0
    remaining_budget = budget
    chosen_items = []
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )
    for item, details in sorted_items:
        if remaining_budget - details["cost"] >= 0:
            total_calories += details["calories"]
            remaining_budget -= details["cost"]
            chosen_items.append(item)
        else:
            break
    return total_calories, budget - remaining_budget, chosen_items


def dynamic_programming(items, budget):
    item_names = list(items.keys())
    dp_table = [[0 for x in range(budget + 1)] for y in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        for b in range(1, budget + 1):
            if items[item_names[i - 1]]["cost"] <= b:
                dp_table[i][b] = max(
                    dp_table[i - 1][b],
                    items[item_names[i - 1]]["calories"]
                    + dp_table[i - 1][b - items[item_names[i - 1]]["cost"]],
                )
            else:
                dp_table[i][b] = dp_table[i - 1][b]

    chosen_items = []
    temp_budget = budget
    i = len(items)
    while i > 0:
        if dp_table[i][temp_budget] != dp_table[i - 1][temp_budget]:
            chosen_items.append(item_names[i - 1])
            temp_budget -= items[item_names[i - 1]]["cost"]
        i -= 1
    return dp_table[len(items)][budget], budget - temp_budget, chosen_items


if __name__ == "__main__":
    budget = 100
    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)
    print(greedy_result, dp_result)
