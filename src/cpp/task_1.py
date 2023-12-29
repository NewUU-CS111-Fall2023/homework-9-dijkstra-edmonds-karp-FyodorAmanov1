import heapq

def dijkstra(graph, start):
    # Initialize distance dictionary with infinite distances for all vertices
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # Priority queue to store vertices and their corresponding distances
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Skip if we have already processed this vertex
        if current_distance > distances[current_vertex]:
            continue
        
        # Update distances for neighboring vertices
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances