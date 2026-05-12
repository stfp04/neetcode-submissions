# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
        
    def mergeTwoLists(self, l1: List[Optional[ListNode]], l2: List[Optional[ListNode]]) -> None:
        i, j = l1, l2

        if j.val < i.val:
            tmp = j.next
            j.next = i
            l1 = i = j
            j = tmp

        while i.next and j:
            nn = i.next
            if nn.val <= j.val:
                i = i.next
            else:
                tmp = j.next
                i.next = j
                j.next = nn
                j = tmp
        
        if j:
            i.next = j

        return l1
   
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or (len(lists) == 0):
            return
        if len(lists) == 1:
            return lists[0]
        
        for i in range(1,len(lists)):
            lists[i] = self.mergeTwoLists(lists[i], lists[i-1])
        return lists[-1]