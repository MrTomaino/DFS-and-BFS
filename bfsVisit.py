def bfsVisit(graph, node): #function for BFS
  visited = [] # List for visited nodes.
  queue = []     #Initialize a queue

  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
