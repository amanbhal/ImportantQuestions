"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""

#=> We need to have the list of all the nodes in the graph given to us. This list of nodes should also have the list
#   of corresponding neighbors.
#   DataStructure to achieve this will bw like: adjList = {node.label: node.neighbors}
#   We use DFS to create the above mentioned list.
#=> Now we need to create new graph. Therefore we first need to create all the nodes and have a way to point each node.
#   For this we again use a dictionary: newGraph = {node.label: node}
#   Now we will use the adjList created above to link all these nodes.

# Definition for a undirected graph node
class UndirectedGraphNode(object):
 def __init__(self, x):
     self.label = x
     self.neighbors = []

def cloneGraph(node):
    """
    :type node: UndirectedGraphNode
    :rtype: UndirectedGraphNode
    """
    if node==None:
        return None
    global adjList
    adjList = {}
    #make the adjacency list using dfs
    dfs(node)
    newGraph = {}
    #create all the nodes for new graph
    for key in adjList.keys():
        x = UndirectedGraphNode(key)
        newGraph[key] = x
    #link all the nodes as they were linked in the old graph
    for nodeLabel in adjList.keys():
        neighborList = adjList[nodeLabel]
        for neighbor in neighborList:
            newGraphNode = newGraph[nodeLabel]
            newGraphNode.neighbors.append(newGraph[neighbor.label])
    return newGraph[node.label]


def dfs(node):
    global adjList
    if node.label not in adjList:
        adjList[node.label] = node.neighbors
        for i in range(len(node.neighbors)):
            dfs(node.neighbors[i])