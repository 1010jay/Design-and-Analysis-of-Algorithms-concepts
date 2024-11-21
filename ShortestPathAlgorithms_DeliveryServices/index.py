import heapq

def dijkstra(graph, start, end):
    # Priority queue to store (distance, vertex)
    pq = []
    heapq.heappush(pq, (0, start))

    # Distances dictionary
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Predecessor dictionary for path reconstruction
    predecessors = {vertex: None for vertex in graph}

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        # If the shortest path to current_vertex is already found
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    # Reconstruct the path
    path = []
    current = end
    while current:
        path.append(current)
        current = predecessors[current]
    path.reverse()

    return distances[end], path

def main():
    # Example graph (adjacency list)
    graph = {
        "Warehouse": {"A": 2, "C": 5},
        "A": {"B": 3},
        "B": {"C": 1, "Delivery": 6},
        "C": {"Delivery": 6},
        "Delivery": {}
    }

    # Compute shortest path
    start, end = "Warehouse", "Delivery"
    distance, path = dijkstra(graph, start, end)

    print(f"Shortest distance from {start} to {end}: {distance}")
    print(f"Path: {' → '.join(path)}")

if __name__ == "__main__":
    main()
