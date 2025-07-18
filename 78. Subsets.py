class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def bt(start,path):
            res.append(list(path))
            for i in range(start,len(nums)):
                path.append(nums[i])
                bt(i+1,path)
                path.pop()
        bt(0,[])
        return res
        