class Node:
    def _init_(self, v, weight):
        self.v=v
        self.weight=weight
class pathNode:
    def _init_(self, node, parent):
        self.node=node
        self.parent=parent
adj = []
ef addEdge(u, v, weight):
    adj[u].append(Node(v, weight))
def GBFS(h, V, src, dest):
    openList = []
    closeList = []
    openList.append(pathNode(src, None))
    while (openList):
        currentNode = openList[0]
        currentIndex = 0
        for i in range(len(openList)):
            if(h[openList[i].node] < h[currentNode.node]):
                currentNode = openList[i]
                currentIndex = i
        openList.pop(currentIndex)
        closeList.append(currentNode)
        if(currentNode.node == dest):
            path = []
            cur = currentNode
            while(cur != None):
                path.append(cur.node)
                cur = cur.parent
            path.reverse()
            return path
        for node in adj[currentNode.node]:
            for x in openList:
                if(x.node == node.v):
                    continue
            for x in closeList:
                if(x.node == node.v):
                    continue
            openList.append(pathNode(node.v, currentNode))
    return []
V = 10
for i in range(V):
    adj.append([])
addEdge(0, 1, 2)
addEdge(0, 2, 1)
addEdge(0, 3, 10)
addEdge(1, 4, 3)
addEdge(1, 5, 2)
addEdge(2, 6, 9)
addEdge(3, 7, 5)
addEdge(3, 8, 2)
addEdge(7, 9, 5)
h = [20, 22, 21, 10, 25, 24, 30, 5, 12, 0]
path = GBFS(h, V, 0, 9)
for i in range(len(path) - 1):
    print(path[i], end = " -> ")
print(path[(len(path)-1)])