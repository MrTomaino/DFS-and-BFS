# see "East Coast Cities.png"
cities={
  'Boston':['New York'],
  'New York':['Philadelphia','Boston'],
  'Philadelphia':['New York','Baltimore','Virginia Beach'],
  'Baltimore':['Washington, D.C.','Philadelphia'],
  'Washington, D.C.':['Richmond','Baltimore'],
  'Richmond':['Raleigh','Virginia Beach','Washington, D.C.'],
  'Virginia Beach':['Raleigh','Richmond','Philadelphia'],
  'Raleigh':['Charlotte','Virginia Beach','Richmond','Jacksonville'],
  'Charlotte':['Atlanta','Raleigh','Jacksonville'],
  'Atlanta':['Jacksonville','Orlando','Tampa','Charlotte'],
  'Jacksonville':['Tampa','Orlando','Atlanta','Miami','Charlotte','Raleigh'],
  'Orlando':['Tampa','Miami','Jacksonville','Atlanta'],
  'Tampa':['Miami','Orlando','Jacksonville','Atlanta'],
  'Miami':['Tampa','Orlando','Jacksonville']
}
       
from dfsPath import *
from bfsShortestPath import *
print()
print()
print("Following is a DFS City Search")
print("Boston to Miami:\n", dfs_path(cities,'Boston','Miami'))
print()
print("Boston to Miami (Shortest Path):\n", bfs_shortest_path(cities,'Boston','Miami'))
