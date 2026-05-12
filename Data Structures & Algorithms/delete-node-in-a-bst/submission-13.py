# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        parent = None
        curr = root
        while curr:
            if key == curr.val:
                break

            parent = curr
            if key > curr.val:
                curr = curr.right
            else:
                curr = curr.left

        if not curr:
            return root

        if not curr.right:
            if not parent:
                return curr.left
            if parent.left and parent.left.val == curr.val:
                parent.left = curr.left
            else:
                parent.right = curr.left
            return root 
        
        right_parent = None
        right_node = curr.right
        while right_node.left:
            right_parent = right_node
            right_node = right_node.left

        curr.val = right_node.val
        if right_parent:
            right_parent.left = None if not right_node.right else right_node.right
        else:
            curr.right = None if not right_node.right else right_node.right
        

        return root

        