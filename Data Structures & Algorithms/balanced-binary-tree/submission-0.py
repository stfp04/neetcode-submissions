# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def heightTree(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            leftHeight = heightTree(root.left)
            rightHeight = heightTree(root.right)

            if -1 in (leftHeight, rightHeight):
                return -1

            if abs(leftHeight - rightHeight) > 1:
                return -1

            return max(rightHeight, leftHeight) + 1

        height = heightTree(root)
        return True if height != -1 else False
        