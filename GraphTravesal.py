from typing import List



class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class GraphTravesal:
    def DFS(self, v: List[int][int]):
        visited = set()
        startingNode = 0
        self.DFSRecurssive(v, visited, startingNode)
        print(visited)

    def DFSRecurssive(self, v: List[int][int], visited: set, node: int):
        for i in range(len(v[node])):
            if v[node][i] == 1 and i not in visited:
                visited.add(i)
                self.DFSRecurssive(v, visited, i)



if __name__ == '__main__':
    GraphTravesal.DFS([[0 , 1 , 0], [0, 1 , 1], [0 , 1 , 0]])