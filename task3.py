import networkx as nx
from collections import deque
import heapq


def print_table(distances):
    print("{:<20} {:<15}".format("Вершина", "Відстань"))
    print("-" * 35)

    for vertex in distances:
        distance = distances[vertex]
        if distance == float("infinity"):
            distance_str = "∞"
        else:
            distance_str = str(f"{distance} км")
        print("{:<20} {:<15}".format(vertex, distance_str))


def dijkstra_with_heap(graph, start_vertex):

    distances = {vertex: float("infinity") for vertex in graph.nodes}
    distances[start_vertex] = 0
    previous_nodes = {vertex: None for vertex in graph.nodes}
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, edge_data in graph[current_vertex].items():
            weight = edge_data.get("weight", 1)
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances, previous_nodes


def reconstruct_path(previous_nodes, start_vertex, end_vertex):
    path = deque()
    current_vertex = end_vertex

    while current_vertex is not None:
        path.appendleft(current_vertex)
        current_vertex = previous_nodes[current_vertex]

    if path[0] == start_vertex:
        return list(path)
    return None


def main():
    G = nx.Graph()

    nodes = ["Kyiv", "Kharkiv", "Kherson", "Odesa", "Lviv", "Vinnytsia"]
    G.add_nodes_from(nodes)

    edges_with_weights = [
        ("Kyiv", "Kharkiv", 479),
        ("Kyiv", "Kherson", 540),
        ("Kyiv", "Odesa", 475),
        ("Kyiv", "Lviv", 540),
        ("Kyiv", "Vinnytsia", 270),
        ("Kharkiv", "Kherson", 565),
        ("Kharkiv", "Odesa", 570),
        ("Kharkiv", "Lviv", 790),
        ("Kherson", "Odesa", 200),
        ("Kherson", "Lviv", 900),
        ("Odesa", "Lviv", 790),
        ("Lviv", "Vinnytsia", 360),
    ]

    G.add_weighted_edges_from(edges_with_weights)

    print("Граф з вагами (відстанями в км):")
    for u, v, data in G.edges(data=True):
        print(f"  {u} -- {v}: {data['weight']} км")

    print("\n" + "=" * 60)
    print("--- Застосування алгоритму Дейкстри з бінарною купою ---")
    print("Знаходження найкоротших відстаней від кожного міста до інших:")

    for city in G.nodes():
        print(f'\nНайкоротші відстані від "{city}":')
        distances_from_city, _ = dijkstra_with_heap(G, city)
        print_table(distances_from_city)

    print("\n" + "=" * 60)
    print("--- Приклад знаходження конкретного найкоротшого шляху ---")
    start_path_node = "Kyiv"
    end_path_node = "Kherson"

    distances, previous_nodes = dijkstra_with_heap(G, start_path_node)
    path = reconstruct_path(previous_nodes, start_path_node, end_path_node)
    length = distances[end_path_node]

    if path and length != float("infinity"):
        print(f"\nНайкоротший шлях з {start_path_node} до {end_path_node}:")
        print(f"  Шлях: {' -> '.join(path)}")
        print(f"  Довжина шляху: {length} км")
    else:
        print(
            f"\nШлях з {start_path_node} до {end_path_node} не знайдено або не існує."
        )

    start_path_node_2 = "Lviv"
    end_path_node_2 = "Kharkiv"

    distances_2, previous_nodes_2 = dijkstra_with_heap(G, start_path_node_2)
    path_2 = reconstruct_path(previous_nodes_2, start_path_node_2, end_path_node_2)
    length_2 = distances_2[end_path_node_2]

    if path_2 and length_2 != float("infinity"):
        print(f"\nНайкоротший шлях з {start_path_node_2} до {end_path_node_2}:")
        print(f"  Шлях: {' -> '.join(path_2)}")
        print(f"  Довжина шляху: {length_2} км")
    else:
        print(
            f"\nШлях з {start_path_node_2} до {end_path_node_2} не знайдено або не існує."
        )


if __name__ == "__main__":
    main()
