# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        if not head:
            return
        cur = head
        while cur is not None: 
            if not res:
                res = ListNode(cur.val)
            else:
                new = ListNode(cur.val, res)
                res = new
            cur = cur.next
        return res