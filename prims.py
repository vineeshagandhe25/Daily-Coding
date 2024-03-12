# Q :Implement Prim’s  algorithms to generate minimum cost spanning tree.

def primsMST(graph):
    vertices=len(graph) # to get no of vertices
    selected=[0]*vertices # to track vertices
    no_of_edges=0 
    selected[0]=True 
    print("Edge : Weight ")
    while (no_of_edges < vertices-1 ):
        minimum=999999999
        x=0
        y=0
        for i in range(vertices):
            if selected[i]:
                  for j in range(vertices):
                      if ( not selected[j] and graph [i][j] ):
                          if minimum > graph[i][j]:
                              minimum=graph[i][j]
                              x=i
                              y=j
        print(x,"-",y,":",graph[x][y])
        selected[y]=True
        no_of_edges += 1

g=[[0,10,0,8],[10,0,12,0],[0,12,0,3],[8,0,3,0]]
primsMST(g)