graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

def bfs(graph, start_node):
    visited = set()  # Use a set for visited nodes.
    queue = [start_node]  # Initialize a queue with the start node.

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])
    
# Main module
print("Following is the Breadth-First Search:")
bfs(graph, '5')  # Function calling
