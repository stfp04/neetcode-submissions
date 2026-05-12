# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def printLinkedList(self, head: ListNode) -> None:
        cur = head
        print("[", end="")
        while cur:
            print(cur.val, end="")
            print(",", end="")
            cur = cur.next
        print("]", end="")

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = list1, list2

        if not h1:
            return h2
        if not h2:
            return h1
        
        c1, c2 = h1, h2
        p1, p2 = None, None

        while c1:
            print("BEGIN")
            print("c1 -", c1.val)

            if c2 is None:
                break
            elif c2.val < c1.val:
                print("COMPARE")
                print("c1.val", c1.val)
                print("c2.val", c2.val)

                tmp = c2.next
                c2.next = c1
                
                if not p1:
                    h1 = c2
                else:
                    p1.next = c2

                p1 = c2
                c2 = tmp
            else:
                print("NOT COMPARE")

                p1 = c1
                c1 = c1.next

            print("AFTER INSERT")
            self.printLinkedList(h1)

            print("END")
        
        if c2:
            p1.next = c2

        return h1
