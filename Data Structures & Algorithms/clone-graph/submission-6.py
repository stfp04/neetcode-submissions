"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldTonew={} #val,newNode
        if not node:
            return None
        
        q=deque()
        oldTonew[node]=Node(node.val)
        q.append(node)
        while q:
            newN=q.popleft()
           
            for neg in newN.neighbors:
                if neg not in oldTonew:
                    
                    oldTonew[neg]=Node(neg.val)
                    q.append(neg)
                oldTonew[newN].neighbors.append(oldTonew[neg])
        

        return oldTonew[node]
        
        
        
       

        