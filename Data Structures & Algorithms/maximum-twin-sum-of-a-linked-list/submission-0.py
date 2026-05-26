# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head.next
        results = [head.val]
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            results.append(slow.val)
        slow = slow.next
        print(results)
        res = 0
        i = len(results) - 1
        while slow:
            res = max(res, results[i] + slow.val)
            i -= 1
            slow = slow.next

        return res
        