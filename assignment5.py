import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define the edges of the graph
edges = [
    (0, 1), (0, 2), (1, 0), (1, 3),
    (2, 0), (3, 1), (4, 1), (4, 3),
    (5, 2), (6, 1), (6, 3), (7, 2),
    (8, 1), (8, 4), (9, 5), (10, 4),
    (11, 3), (11, 6), (12, 5), (13, 7),
    (13, 8), (14, 4), (15, 5), (16, 8),
    (17, 9), (18, 10), (19, 10), (19, 11),
    (20, 11), (21, 10), (21, 11), (22, 12),
    (23, 11), (24, 10), (25, 13), (25, 14),
    (26, 14), (27, 13), (28, 14), (28, 16),
    (29, 15), (30, 14), (31, 15), (32, 15),
    (33, 16), (34, 17), (35, 18), (36, 18),
    (37, 19), (38, 21), (38, 22), (39, 22),
    (40, 21), (41, 0), (42, 0), (43, 0),
    (44, 0), (45, 0), (46, 0), (47, 0),
    (48, 0), (49, 0), (50, 0), (51, 0),
    (52, 0), (53, 0), (54, 0), (55, 0),
    (56, 0), (57, 0), (58, 0), (59, 0)
]

# Add edges to the graph
G.add_edges_from(edges)

# Calculate PageRank
pagerank = nx.pagerank(G, alpha=0.85)

# Print the PageRank scores
print(pagerank)
