from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def clone (node):
            if node in oldToNew : return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy
        return clone(node) if node else None
    
# TC : O(V+E) (number of vertices + nummber of edges)
# SC : O(V) ( stores all nodes hence = number of vertices)