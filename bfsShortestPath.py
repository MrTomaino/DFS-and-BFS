# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
  print("Visiting: ",end='')
  # keep track of explored nodes
  explored = []
  # keep track of all the paths to be checked
  queue = [[start]]
  print(start,'',end='')

  # return path if start is goal
  if start == goal:
      return "That was easy! Start = goal"

  # keeps looping until all possible paths have been checked
  while queue:
      # pop the first path from the queue
      path = queue.pop(0)
      # get the last node from the path
      node = path[-1]
      if node not in explored:
          neighbours = graph[node]
          # go through all neighbour nodes, construct a new path and
          # push it into the queue
          for neighbour in neighbours:
              print(neighbour,'',end='')
              new_path = list(path)
              new_path.append(neighbour)
              queue.append(new_path)
              # return path if neighbour is goal
              if neighbour == goal:
                  print()
                  return new_path

          # mark node as explored
          explored.append(node)

  # in case there's no path between the 2 nodes
  return "So sorry, but a connecting path doesn't exist :("
