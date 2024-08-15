import numpy as np
mat = np.array([[0,1,1,0,0],[1,0,1,0,1],[1,1,0,0,0],[0,0,0,0,1],])
print(mat)
def dfs(graph,start,visited = None):
  if visited is None:
    visited = set()

  visited.add(start)
  print(start,end='')

  for adjacent in graph[start]:   #adjacent B,adjacent
    if adjacent not in visited:
      dfs(graph,adjacent,visited)
graph = {
    'A':['B','C'],
    'B':['A','C','E'],
    'C':['A','B'],
    'D':['E'],
    'E':['B','D']
}
print(graph)
start_node = 'A'
print('starting DFS from start node:',start_node)
dfs(graph,start_node)