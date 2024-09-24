# see "Directional Graph A through I.png"
graph={
  'A':['B','C'],
  'B':['D','E'],
  'C':['F','G'],
  'D':[],
  'E':['H'],
  'F':['C','E','I'],
  'G':[],
  'H':[],
  'I':['G']
}

#from dfsVisit import *
#print("Following is the Depth-First Traversal")
#dfsVisit(graph, 'A')    # function calling
#print()
#print()

#from bfsVisit import *
#print("Following is the Breadth-First Traversal")
#bfsVisit(graph, 'A')    # function calling
#print()

#print()
#print()


#from dfsPath import *
#print()
#print()
#print("Following is the Depth-First Search")
#print(dfs_path(graph, 'A', 'H')  )

#from bfsShortestPath  import *
#print()
#print()
#print("Following is the Breadth-First Search")
#print(bfs_shortest_path(graph, 'A', 'H')  )




