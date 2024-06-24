# To find Topological order of a given graph.
'''A topological sort or topological ordering of a directed graph is a linear ordering of its vertices in which u occurs before v in the ordering for every 
directed edge uv from vertex u to vertex v. 
'''
def topological_sort(graph):
    visited = [False] * len(graph)
    stack = []

    for vertex in range(len(graph)):
        if not visited[vertex]:
            dfs(graph, vertex, visited, stack)

    return stack[::-1]

def dfs(graph, vertex, visited, stack):
    visited[vertex] = True

    for adjacent in graph[vertex]:
        if not visited[adjacent]:
            dfs(graph, adjacent, visited, stack)

    stack.append(vertex)


graph = [
    [1, 2], 
    [3],     
    [3],     
    []       
]

res = topological_sort(graph)
print(res)  


