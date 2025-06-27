# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        
        result = []
        rev=False

        if not root:
            return result
        q=deque([root])
        
        while q:
            temp = []
            n=len(q)

            for _ in range(n):
                node= q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if rev:
                result.append(temp[::-1])
            else:
                result.append(temp)
            rev = not rev
        return result



        