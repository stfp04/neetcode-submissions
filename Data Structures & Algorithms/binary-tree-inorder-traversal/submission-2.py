# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorderTraversalAux(result: List, root: Optional[TreeNode]):
            if not root:
                return
            inorderTraversalAux(result, root.left)
            result.append(root.val)
            inorderTraversalAux(result, root.right)
        
        result = []
        inorderTraversalAux(result, root)
        return result

