import heapq

def find_shortest_path_with_fuel(n, flights, src, dst, k, fuel):
    graph = {i: [] for i in range(n)}

    for u, v, distance, ars in flights:
        graph[u].append((v, distance, ars))

    priority_queue = [(0, src, k + 1, fuel)]

    while priority_queue:
        cost, current, stops_left, remaining_fuel = heapq.heappop(priority_queue)

        if current == dst:
            return cost

        if stops_left > 0:
            for neighbor, distance, ars in graph[current]:
                new_fuel = remaining_fuel - distance
                if new_fuel >= 0 or (new_fuel < 0 and ars == 1):
                    heapq.heappush(priority_queue, (cost + distance, neighbor, stops_left - 1, fuel))

    return -1
