# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        rootValue = preorder[0]
        root = TreeNode(rootValue)

        leftInorder, rightInorder = [], []
        currInorder = leftInorder
        for i in range(len(inorder)):
            el = inorder[i]
            if el == rootValue:
                currInorder = rightInorder
                continue
            currInorder.append(el)

        leftPreorder, rightPreorder = preorder[1:len(leftInorder) + 1], preorder[len(leftInorder) + 1:]

        root.left = self.buildTree(leftPreorder, leftInorder)
        root.right = self.buildTree(rightPreorder, rightInorder)
        return root
        

        

        
            
        
