# To check whether given node is Articulation Point or not .

def is_articulation_point(graph, node):
    # removing the given node from graph and also removing its associated egdes from graph and checking whether graph is connected or not .
       
    graph_without_node = {n: [neighbor for neighbor in neighbors if neighbor != node]   # Time Complexity - O(n^2) 
                          for n, neighbors in graph.items() if n != node}

    def is_connected(graph):
        visited = set()
        # here dfs stands for depth first search 
        # need to calculate time and space complexities .
        def dfs(v):
            visited.add(v)
            for neighbor in graph[v]:
                if neighbor not in visited:
                    dfs(neighbor)

        
        remaining_nodes = list(graph.keys()) # extracting only nodes from graph 
        if not remaining_nodes: # condition to check is graph empty
            return False

        
        dfs(remaining_nodes[0]) # calling dfs to check graph is connected or not 

        
        return len(visited) == len(graph)

    
    return not is_connected(graph_without_node)


graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

node = 2

if is_articulation_point(graph, node):
    print(f"The node {node} is an articulation point.")
else:
    print(f"The node {node} is not an articulation point.")
