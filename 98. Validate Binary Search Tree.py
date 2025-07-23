# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.is_valid_bst_helper(root, float('-inf'), float('inf'))

    def is_valid_bst_helper(self,node,min_val,max_val):
        if node is None:
            return True

        if not (min_val < node.val < max_val):
            return False
        
        left_is_valid = self.is_valid_bst_helper(node.left, min_val, node.val)
        right_is_valid = self.is_valid_bst_helper(node.right, node.val, max_val)
        
        return left_is_valid and right_is_valid
