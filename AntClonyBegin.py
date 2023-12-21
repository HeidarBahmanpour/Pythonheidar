import random

# تعریف گراف (نمایش محیط)
graph = {
    'A': {'B': 1, 'C': 2},
    'B': {'A': 1, 'C': 3, 'D': 4},
    'C': {'A': 2, 'B': 3, 'D': 1},
    'D': {'B': 4, 'C': 1}
}

# تعریف تعداد مورچگان
num_ants = 5

# تعریف تعداد چرخه‌ها
num_iterations = 100

# شروع اجرای الگوریتم
for iteration in range(num_iterations):
    # ایجاد مسیرهای تصادفی برای هر مورچه
    ant_paths = {ant: [] for ant in range(num_ants)}

    for ant in range(num_ants):
        current_node = random.choice(list(graph.keys()))

        for _ in range(len(graph) - 1):
            neighbor_nodes = list(graph[current_node].keys())
            next_node = random.choice(neighbor_nodes)
            ant_paths[ant].append((current_node, next_node, graph[current_node][next_node]))
            current_node = next_node

    # محاسبه طول مسیرها
    path_lengths = [sum(edge[2] for edge in ant_paths[ant]) for ant in range(num_ants)]

    # انتخاب بهترین مسیر
    best_path = ant_paths[path_lengths.index(min(path_lengths))]
    best_path_length = min(path_lengths)

    print(f"Iteration {iteration + 1}: Best Path {best_path}, Length {best_path_length}")
