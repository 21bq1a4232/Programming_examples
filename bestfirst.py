from queue import PriorityQueue
def best_first_search(graph, start_node):
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((0, start_node))  # Enqueue start node with priority 0
    while not priority_queue.empty():
        _, current_node = priority_queue.get()  # Dequeue node with highest priority
        if current_node not in visited:
            print(current_node)  # Process the current node
            visited.add(current_node)
            neighbors = graph[current_node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    priority_queue.put((ord(neighbor), neighbor))
g = {
    'A': ['B', 'D'],
    'B': ['C', 'E', 'G'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'F': [],
    'G': ['F'],
    'H': ['G', 'F']
}
start_node = 'A'
best_first_search(g, start_node)