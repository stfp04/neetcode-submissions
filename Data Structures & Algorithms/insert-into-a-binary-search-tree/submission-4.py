# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        curr = root
        next_node = curr.left if val < curr.val else curr.right
        while next_node:
            curr = next_node
            next_node = curr.left if val < curr.val else curr.right
        if val > curr.val:
            curr.right = TreeNode(val)
        else:
            curr.left = TreeNode(val)
        return root
