def dfsVisit(graph, node): #function for BFS
  visited = [] # List for visited nodes.
  stack = []     #Initialize a stack

  visited.append(node)
  stack.append(node)

  while stack:          # Creating loop to visit each node
    m = stack.pop(-1) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        stack.append(neighbour)
