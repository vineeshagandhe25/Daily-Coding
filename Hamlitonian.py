# Hamiltonian  Cycle
NODE = 5
graph = [
    [0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 1, 0, 1, 0]
]
path = [None] * NODE

# Function to display the Hamiltonian cycle
def displayCycle():
    print("Cycle Found:", end=" ")
    for i in range(NODE):
        print(path[i], end=" ")
    # Print the first vertex again
    print(path[0])

# Function to check if adding vertex v to the path is valid
def isValid(v, k):
    # If there is no edge between path[k-1] and v
    if graph[path[k - 1]][v] == 0:
        return False
    # Check if vertex v is already taken in the path
    for i in range(k):
        if path[i] == v:
            return False
    return True

# Function to find the Hamiltonian cycle
def cycleFound(k):
    # When all vertices are in the path
    if k == NODE:
        # Check if there is an edge between the last and first vertex
        if graph[path[k - 1]][path[0]] == 1:
            return True
        else:
            return False
    # adding each vertex (except the starting point) to the path
    for v in range(1, NODE):
        if isValid(v, k):
            path[k] = v
            if cycleFound(k + 1):
                return True
            # Remove v from the path
            path[k] = None
    return False

# Function to find and display the Hamiltonian cycle
def hamiltonianCycle():
    for i in range(NODE):
        path[i] = None
    # Set the first vertex as 0
    path[0] = 0
    if not cycleFound(1):
        print("Solution does not exist")
        return False
    displayCycle()
    return True

if __name__ == "__main__":
    hamiltonianCycle()