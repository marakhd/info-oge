import heapq
from typing import List, Dict
import networkx as nx

class NumFour:
    @staticmethod
    def find_shortest_path(graph: Dict[str, Dict[str, int]], start: str, end: str):
        # Начальная настройка
        priority_queue = [(0, start)]  # Очередь с приоритетами (расстояние, вершина)
        distances = {vertex: float('inf') for vertex in graph}  # Минимальное расстояние до каждой вершины
        distances[start] = 0
        visited = set()  # Посещенные вершины

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Если вершина уже обработана, пропускаем
            if current_vertex in visited:
                continue
            
            visited.add(current_vertex)

            # Проверяем соседей
            for neighbor, weight in graph[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        print(distances[end])  # Возвращаем расстояние до конечной точки
        return distances

    @staticmethod
    def find_shortest_path_with_nx(edges: List[tuple], start: str, end: str):
        # Создаем граф
        graph = nx.Graph()

        # Добавляем ребра в граф
        graph.add_weighted_edges_from(edges)

        # Нахождение кратчайшего пути между A и F
        shortest_path_length = nx.dijkstra_path_length(graph, start, end)  # Длина пути
        shortest_path = nx.dijkstra_path(graph, start, end)  # Сам путь

        # Результат
        print(f"Кратчайшее расстояние между {start} и {end}: {shortest_path_length}")
        print(f"Путь: {' -> '.join(shortest_path)}")
        
        return {
            "path_length": shortest_path_length,
            "path": shortest_path
        }
