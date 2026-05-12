# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
"""

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead

# 0
# else -> new_head = rl(1)
# 1
# else -> new_head = rl(2)
# 2
# else -> new_head = rl(3)
# 3
# if -> return 3
# 2
# 2.next(3).next (None) = 2 ; return 3
# 1
# 1.next(2).next(3) = 1 ; return 3
# 0
# 0.next(1).next(2) = 0 ; return 3














