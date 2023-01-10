class GivingTreeOfError:
    def parseInput(self):
        adjList = {}
        tree = input()
        tree = tree.split(" ")
        for i in range(len(tree)):
            if len(tree[i]) < 5 or tree[i][0] != "(" and tree[i][4] != ")" or tree[i][2] != ",":
                return "E1"
            elif tree[i][1] not in adjList:
                adjList[tree[i][1]] = []
            if tree[i][1] not in nodes:
                nodes.append(tree[i][1])
                visited[tree[i][1]] = 0
            if tree[i][3] not in nodes:
                nodes.append(tree[i][3])
                visited[tree[i][3]] = 0
            if tree[i][3] in adjList[tree[i][1]]:
                return "E2"
            elif tree[i][3] not in adjList[tree[i][1]]:
                adjList[tree[i][1]].append(tree[i][3])
            if len(adjList[tree[i][1]]) > 2:
                return "E3"
        return adjList

    def multipleRoots(self, adjList):
        root = nodes[0]
        result = ""
        self.dfs(root, adjList, result)
        if 0 in visited.values():
            return "E4"
        else:
            return result

    def dfs(self, node, adjList, result) -> str:
        visited[node] = 1
        result += "("+node
        if node in adjList:
            for n in adjList[node]:
                if visited[n] == 1:
                    return "E5"
                result = self.dfs(n, adjList, result)
        result += ")"
        return result


if __name__ == '__main__':
    nodes = []
    visited = {}
    obj = GivingTreeOfError()
    a = obj.parseInput()
    if a is not str:
        a = obj.multipleRoots(a)
    print(a)
