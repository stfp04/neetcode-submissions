class Node:
    def __init__(self, n=0, c=0):
        self.n = n
        self.c = c
        self.next, self.prev = None, None

class Solution:
    def _print(self, left):
        print("[", end="")
        curr = left.next
        while curr.n != None:
            print(f"{curr.n}({curr.c})", end=",")
            curr = curr.next
        print("]")

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
            print()
            print("Num", num)
            if num not in numCount:
                print("Not In")
                node = Node(num, 1)
                numCount[num] = node
                if size >= k:
                    continue
                print("Before Insert")
                self._print(left)
                self._insert(left, node)
                print("After Insert")
                self._print(left)
                size += 1
            else:
                print("In")
                node = numCount[num]
                node.c += 1

                if node.prev and node.next:
                    print("Inside List")
                    print("Before Swap")
                    self._print(left)
                    while node.c > node.next.c and node.next.n != None:
                        print("Before each Swap")
                        self._print(left)
                        self._swap(node, node.next)
                        print("After each swap")
                        self._print(left)
                elif size >= k:
                    print("Not inside")
                    if node.c <= left.next.c:
                        continue
                    print("Before remove")
                    self._print(left)
                    self._remove(left, left.next)
                    print("After Remove")
                    self._print(left)
                    print("Before Insert")
                    self._insert(left, node)
                    self._print(left)
                    while node.c > node.next.c and node.next.n != None:
                        print("Before each Swap")
                        self._print(left)
                        self._swap(node, node.next)
                        print("After each swap")
                        self._print(left)
            
        res = []
        curr = left.next
        while curr.n != None:
            res.append(curr.n)
            curr = curr.next
        
        return res

    