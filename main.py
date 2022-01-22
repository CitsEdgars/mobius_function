from collections import defaultdict
from logging.config import valid_ident
from turtle import st

all_paths = []

class Graph:
  
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
  
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printAllPathsUtil(self, u, d, visited, path):
        visited[u]= True
        path.append(u)
        global all_paths
 
        if u == d:
            new = []
            for i in path:
                new.append(i)
            all_paths.append(new)
        else:
            for i in self.graph[u]:
                if visited[i]== False:
                    self.printAllPathsUtil(i, d, visited, path)
                     
        path.pop()
        visited[u]= False
  
  
    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):
        visited =[False]*(self.V)
        path = []
        self.printAllPathsUtil(s, d, visited, path)
  

elements = -1
matrix = []
with open("ieeja.txt", "r") as infile: 
    for idx, line in enumerate(infile):
        matrix_row = []
        if idx == 0: elements = int(line)
        else:
            less_or_equal = line
            for i in less_or_equal:
                if i in ["0","1"]:
                    matrix_row.append(int(i))
        matrix.append(matrix_row)
    matrix.remove([])

g = Graph(elements)
# for row in matrix: print(row)
for idx_row, row in enumerate(matrix):
    for idx_col, col in enumerate(row):
        if col == 1:
            g.addEdge(idx_row, idx_col)

for idx_row, row in enumerate(matrix):
    for idx_col, col in enumerate(row):
        if col == 1:
            g.printAllPaths(idx_row, idx_col)


intervals = {}
mobius_values = []
for idx_row, row in enumerate(matrix):
    mobius_row = []
    for idx_col, col in enumerate(row):
        mobius_row.append("N/A")
    mobius_values.append(mobius_row)


for path in all_paths:
    # print("-------------------")
    start = path[0] 
    end = path[-1]
    # print(start, end, mobius_values[start][end])
    if len(path) == 1:
        mobius_values[start][end] = 1
    elif len(path) == 2:
        if mobius_values[start][end] != "N/A":
            mobius_values[start][end] += -mobius_values[start][start]
        else:
            mobius_values[start][end] = -mobius_values[start][start]
    else:
        value = 0
        if mobius_values[start][end] != "N/A":
            value = mobius_values[start][end]
        for idx, node in enumerate(path):
            if node == path[0] or node == end: continue
            if path[idx+1] == end:
                value += -mobius_values[start][node]
                # print(start, node, path, value, mobius_values[start][node])
        mobius_values[start][end] = value

    # print(start, end, mobius_values[start][end])


for idx_row, row in enumerate(mobius_values):
    for idx_col, col in enumerate(row):
        if col != "N/A": 
            intervals["[{},{}]".format(idx_row + 1 , idx_col + 1)] = col

# for row in mobius_values: print(row)
with open("izeja.txt", "w") as outfile: 
    for i in intervals.keys():
        outfile.write("{} {}\n".format(i, intervals[i]))