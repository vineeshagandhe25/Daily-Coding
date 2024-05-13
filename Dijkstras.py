def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current_node = pq.pop(0)
        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                pq.append((distance, neighbor))
                pq.sort()

    return distances


graph = {
    'A': {'B': 3, 'C': 2},
    'B': {'A': 3, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 4},
    'D': {'B': 5, 'C': 4}
}
start_node = 'A'
shortest_distances = dijkstra(graph, start_node)
print("Shortest distances from node", start_node + ":")
for node, distance in shortest_distances.items():
    print("To node", node + ":", distance)
