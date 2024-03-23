import heapq
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge("A", "B", weight=1)
G.add_edge("B", "C", weight=2)
G.add_edge("C", "D", weight=3)


def dijkstra(graph, start):
    shortest_paths = {vertex: float("infinity") for vertex in graph}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        (current_distance, current_vertex) = heapq.heappop(priority_queue)
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight["weight"]
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return shortest_paths


shortest_paths = dijkstra(G, "A")
print(shortest_paths)

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=2)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

plt.axis("off")
plt.show()
