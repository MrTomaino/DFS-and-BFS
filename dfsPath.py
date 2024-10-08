# finds shortest path between 2 nodes of a graph using BFS
def dfs_path(graph, start, goal):
  print("Visiting: ",end='')
  # keep track of explored nodes
  explored = []
  # keep track of all the paths to be checked
  stack = [[start]]

  # return path if start is goal
  if start == goal:
      return "That was easy! Start = goal"

  # keeps looping until all possible paths have been checked
  while stack:
      # pop the last path from the stack
      path = stack.pop(-1)
      # get the last node from the path
      node = path[-1]
      if node not in explored:
          print(node,'',end='')

          neighbours = graph[node]
          # go through all neighbour nodes, construct a new path and
          # push it into the stack
          for neighbour in neighbours:
              new_path = list(path)
              new_path.append(neighbour)
              stack.append(new_path)
              # return path if neighbour is goal
              if neighbour == goal:
                  print(neighbour)
                  return new_path

          # mark node as explored
          explored.append(node)

  # in case there's no path between the 2 nodes
  return "So sorry, but a connecting path doesn't exist :("
