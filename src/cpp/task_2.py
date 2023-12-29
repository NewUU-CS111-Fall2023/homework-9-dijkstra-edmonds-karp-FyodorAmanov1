from collections import deque

def edmonds_karp(graph, source, sink):
    def augment_path(parents, u, v, flow):
        if u == source:
            return flow
        flow = min(flow, graph[parents[v]][v])
        return augment_path(parents, u, parents[v], flow)

    max_flow = 0

    while True:
        # Breadth-First Search to find augmenting paths
        queue = deque([source])
        parents = {vertex: None for vertex in graph}
        parents[source] = source

        while queue:
            current = queue.popleft()
            for neighbor, capacity in graph[current].items():
                if parents[neighbor] is None and capacity > 0:
                    parents[neighbor] = current
                    queue.append(neighbor)
                    if neighbor == sink:
                        break

        # If no augmenting path is found, break out of the loop
        if parents[sink] is None:
            break

        # Find the maximum flow along the augmenting path
        path_flow = augment_path(parents, source, sink, float('inf'))

        # Update residual capacities and reverse edges
        v = sink
        while v != source:
            u = parents[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u

        max_flow += path_flow

    return max_flow
