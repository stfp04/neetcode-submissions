# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def kthInorderTraversal(root: Optional[TreeNode], value, k):
            if not root:
                return (False, value)

            found, leftValue = kthInorderTraversal(root.left, 0, k)
            if found:
                return (found, leftValue)

            nodeValue = value + leftValue + 1
            if nodeValue == k:
                return (True, root.val)
            
            found, rightValue = kthInorderTraversal(root.right, nodeValue, k)
            if found:
                return (found, rightValue)

            return (False, rightValue)

        _, value = kthInorderTraversal(root, 0, k)
        return value
            
