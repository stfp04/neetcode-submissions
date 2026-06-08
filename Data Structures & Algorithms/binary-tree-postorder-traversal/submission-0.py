# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visit = [False]
        res = []

        while stack:
            node, visited = stack.pop(), visit.pop()
            if node: 
                if visited:
                    res.append(node.val)
                else:
                    stack.append(node)
                    visit.append(True)
                    stack.append(node.right)
                    visit.append(False)
                    stack.append(node.left)
                    visit.append(False)

        return res
