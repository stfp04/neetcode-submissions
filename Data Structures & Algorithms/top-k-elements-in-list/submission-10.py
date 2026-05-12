class Node:
    def __init__(self, n=0, c=0):
        self.n = n
        self.c = c
        self.next, self.prev = None, None

class Solution:

    def _insert(self, left, node):
        node.next = left.next
        left.next = node
        node.prev = left
        node.next.prev = node

    def _remove(self, left, node):
        left.next = node.next
        node.next.prev = left
        node.next = node.prev = None

    def _swap(self, node1, node2):
        prev = node1.prev
        after = node2.next
        
        prev.next = node2
        node2.prev = prev
        node2.next = node1
        node1.prev = node2
        node1.next = after
        after.prev = node1

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        left, right = Node(None, -1), Node(None, -1)
        left.next = left.prev = right
        right.next = right.prev = left
        size = 0

        numCount = {}
        
        for num in nums:
            if num not in numCount:
                node = Node(num, 1)
                numCount[num] = node
                if size >= k:
                    continue
                self._insert(left, node)
                size += 1
            else:
                node = numCount[num]
                node.c += 1

                if node.prev and node.next:
                    while node.c > node.next.c and node.next.n != None:
                        self._swap(node, node.next)
                elif size >= k:
                    if node.c <= left.next.c:
                        continue
                    self._remove(left, left.next)
                    self._insert(left, node)
                    while node.c > node.next.c and node.next.n != None:
                        self._swap(node, node.next)
            
        res = []
        curr = left.next
        while curr.n != None:
            res.append(curr.n)
            curr = curr.next
        
        return res

    