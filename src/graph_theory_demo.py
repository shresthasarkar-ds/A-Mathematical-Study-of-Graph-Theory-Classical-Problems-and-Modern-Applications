import heapq
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Weighted graph used throughout Chapter 4
edges = [("A","B",4), ("A","C",2), ("B","C",1), ("B","D",5),
         ("C","D",8), ("C","E",10), ("D","E",2)]
G = nx.Graph()
G.add_weighted_edges_from(edges)

# 1. Representations
nodes = sorted(G.nodes())
A = nx.to_numpy_array(G, nodelist=nodes, weight=None).astype(int)
print("Adjacency matrix (order A..E):\n", A)
print("Degrees:", dict(G.degree()))
print("Adjacency list:", {v: sorted(G[v]) for v in nodes})

# 2. BFS and DFS (unweighted tree-like graph of Fig. 6.3)
T = nx.Graph([("A","B"),("A","C"),("B","D"),("B","E"),("C","F")])
print("BFS order:", ["A"] + [v for u, v in nx.bfs_edges(T, "A")])
print("DFS order:", ["A"] + [v for u, v in nx.dfs_edges(T, "A")])

# 3. Dijkstra written from first principles
def dijkstra(graph, src):
    dist = {v: float("inf") for v in graph}
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, attr in graph[u].items():
            nd = d + attr["weight"]
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
print("Dijkstra from A:", dijkstra(G, "A"))
print("NetworkX check:", nx.dijkstra_path(G, "A", "E"),
      nx.dijkstra_path_length(G, "A", "E"))

# 4. Minimum spanning tree
mst = nx.minimum_spanning_tree(G)
print("MST edges:", sorted(mst.edges(data="weight")),
      "total =", mst.size(weight="weight"))

# 5. Maximum flow
F = nx.DiGraph()
for u, v, c in [("s","a",5),("s","b",4),("a","b",2),("a","t",3),("b","t",5)]:
    F.add_edge(u, v, capacity=c)
print("Maximum flow value:", nx.maximum_flow_value(F, "s", "t"))

# 6. Visualisation
pos = nx.spring_layout(G, seed=7)
path = nx.dijkstra_path(G, "A", "E")
pe = list(zip(path, path[1:]))
nx.draw(G, pos, with_labels=True, node_color="#dbe9f6", edge_color="#9aa9b5")
nx.draw_networkx_edges(G, pos, edgelist=pe, edge_color="red", width=3)
nx.draw_networkx_edge_labels(G, pos, nx.get_edge_attributes(G, "weight"))
import os; os.makedirs("outputs", exist_ok=True)
plt.savefig("outputs/shortest_path.png", dpi=200)
