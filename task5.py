import uuid
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb, to_hex
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


# From heap
def draw_tree_from_heap(heap):
    if not heap:
        return None

    nodes = [Node(val) for val in heap]
    for i in range(len(heap)):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2
        if left_idx < len(heap):
            nodes[i].left = nodes[left_idx]
        if right_idx < len(heap):
            nodes[i].right = nodes[right_idx]
    return nodes[0]


# Generate gradient
def get_gradient_colors(quantity, start="#780056", end="#fbcaed"):
    start_rgb = to_rgb(start)
    end_rgb = to_rgb(end)

    gradient = []
    for i in range(quantity):
        ratio = i / (quantity - 1) if quantity > 1 else 0
        rgb = tuple(
            start_rgb[j] + (end_rgb[j] - start_rgb[j]) * ratio for j in range(3)
        )
        gradient.append(to_hex(rgb))
    return gradient


# BFS
def bfs_visualize(root):
    if not root:
        return []

    queue = deque([root])
    visited = []

    while queue:
        node = queue.popleft()
        visited.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    colors = get_gradient_colors(len(visited))
    for i, node in enumerate(visited):
        node.color = colors[i]

    draw_tree(root)


# DFS
def dfs_visualize(root):
    if not root:
        return []

    stack = [root]
    visited = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    colors = get_gradient_colors(len(visited))
    for i, node in enumerate(visited):
        node.color = colors[i]

    draw_tree(root)


arr = [0, 4, 1, 5, 10, 3]
root = draw_tree_from_heap(arr)
print("Обхід у ширину (BFS)")
bfs_visualize(root)
print("Обхід у глибину (DFS)")
dfs_visualize(root)
