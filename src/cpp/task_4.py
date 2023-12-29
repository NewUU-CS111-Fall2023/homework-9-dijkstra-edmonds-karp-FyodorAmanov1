import heapq

def network_delay_time(times, n, k):
    graph = {i: [] for i in range(1, n + 1)}

    for u, v, w in times:
        graph[u].append((v, w))

    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[k] = 0

    priority_queue = [(0, k)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    max_distance = max(distances.values())

    return max_distance if max_distance < float('inf') else -1