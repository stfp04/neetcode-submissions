"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        if not node.neighbors:
            return Node(val=1, neighbors=None)

        nodes = {}
        visit = set()
        queue = deque()
        queue.append(node)
        first = None
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                visit.add(node.val)

                copy_node = None
                if node.val not in nodes:
                    new_node = Node(val=node.val)
                    copy_node = new_node
                    nodes[node.val] = Node(val=node.val)

                    if not first:
                        first = new_node
                else:
                    copy_node = nodes[node.val]

                for n in node.neighbors:
                    if n.val in visit:
                        continue

                    if n.val not in nodes:
                        new_node = Node(val=n.val, neighbors = [copy_node])
                        copy_node.neighbors.append(new_node)
                        nodes[n.val] = new_node
                    else:
                        nodes[n.val].neighbors.append(copy_node)
                        copy_node.neighbors.append(nodes[n.val])
                    queue.append(n)
        return first




