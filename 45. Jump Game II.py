class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        farthest, currentEnd, jumps = 0,0,0
        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i] )
            if i == currentEnd:
                jumps+=1
                currentEnd = farthest
        return jumps
        