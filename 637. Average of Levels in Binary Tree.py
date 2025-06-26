# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        result = []
        queue = deque([root])
        while queue:
            lvl_size = len(queue)
            lvl_sum = 0
            for _ in range(lvl_size):
                node=queue.popleft()
                lvl_sum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            avg = lvl_sum / float(lvl_size)

            result.append(avg)
        return result

