import networkx as nx

def calculate_degree_centrality(traffic_graph):
    # Calculate degree centrality
    degree_centrality = nx.degree_centrality(traffic_graph)
    return degree_centrality

def main():
    # Create a traffic network graph (undirected)
    traffic_graph = nx.Graph()

    # Add intersections and roads (edges)
    roads = [
        ("A", "B"), ("A", "C"), ("B", "C"),
        ("B", "D"), ("C", "D"), ("D", "E"),
        ("E", "F"), ("C", "F"), ("F", "G")
    ]

    traffic_graph.add_edges_from(roads)

    # Calculate degree centrality
    centrality = calculate_degree_centrality(traffic_graph)

    # Display degree centrality
    print("Degree Centrality (Traffic Analysis):")
    for intersection, centrality_score in centrality.items():
        print(f"Intersection {intersection}: {centrality_score:.2f}")

if __name__ == "__main__":
    main()
