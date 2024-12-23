from info_oge.four import NumFour

# Пример графа в виде словаря
graph = {
    'A': {'C': 8, 'D': 10},
    'B': {'D': 4, 'E': 1},
    'C': {'A': 8, 'D': 1, 'E': 3},
    'D': {'A': 10, 'B': 4, 'C': 1},
    'E': {'B': 1, 'C': 3},
}

# Поиск кратчайшего пути между A и F
start, end = 'A', 'B'
NumFour.find_shortest_path(graph, start, end)

# or

edges = [
    ('A', 'B', 6),
    ('A', 'C', 4),
    ('A', 'D', 2),
    ('B', 'C', 1),
    ('C', 'D', 3),
    ('C', 'F', 1),
    ('D', 'E', 1),
    ('E', 'F', 6),
]

NumFour.find_shortest_path_with_nx(edges, 'A', 'F')