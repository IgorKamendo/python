graph = {"A": ["B", "C", "E"], "B": ["A", "D", "E"], "C": ["A", "F", "G"], "D": ["B"], "E": ["A", "B", "D"], "F": ["C"],
         "G": ["C"]}


def bfs_connected_component(graph, start):
    explored = []
    queue = [start]

    # levels = {}
    # levels[start] = 0

    # visited = [start]

    while queue:
        node = queue.pop(0)
        if node not in explored:
            explored.append(node)
            neighbours = graph[node]

            for neighbour in neighbours:
                #if neighbour not in visited:
                queue.append(neighbour)
                #visited.append(neighbour)

                #levels[neighbour] = levels[node] + 1
                #print(levels)

    return explored


ans = bfs_connected_component(graph, "A")
print(ans)
