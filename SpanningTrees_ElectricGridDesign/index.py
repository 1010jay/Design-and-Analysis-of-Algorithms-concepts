import networkx as nx

def compute_mst(graph):
    # Compute the minimum spanning tree using Kruskal's algorithm
    mst = nx.minimum_spanning_tree(graph, algorithm='kruskal')
    return mst

def main():
    # Create a weighted graph (representing cities and connection costs)
    graph = nx.Graph()

    # Add edges with weights (costs)
    edges = [
        ("City1", "City2", 10),
        ("City1", "City3", 15),
        ("City2", "City3", 5),
        ("City2", "City4", 10),
        ("City3", "City4", 10),
        ("City4", "City5", 20)
    ]

    graph.add_weighted_edges_from(edges)

    # Compute the MST
    mst = compute_mst(graph)

    # Display the edges in the MST and their weights
    print("Minimum Spanning Tree:")
    for edge in mst.edges(data=True):
        print(f"{edge[0]} - {edge[1]}: {edge[2]['weight']}")

if __name__ == "__main__":
    main()
