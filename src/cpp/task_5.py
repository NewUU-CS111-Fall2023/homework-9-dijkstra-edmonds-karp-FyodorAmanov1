import heapq

def find_cheapest_price(n, flights, src, dst, k):
    graph = {i: [] for i in range(n)}

    for u, v, w in flights:
        graph[u].append((v, w))

    priority_queue = [(0, src, k + 1)]

    while priority_queue:
        cost, current, stops_left = heapq.heappop(priority_queue)

        if current == dst:
            return cost

        if stops_left > 0:
            for neighbor, price in graph[current]:
                heapq.heappush(priority_queue, (cost + price, neighbor, stops_left - 1))

    return -1