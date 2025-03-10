class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        res = []
        temp_start = nums[0] 

        for i in range(1,len(nums)+1):
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                if temp_start == nums[i - 1]:
                    res.append(str(temp_start))  
                else:
                    res.append("{}->{}".format(temp_start, nums[i - 1]))
                if i < len(nums):
                    temp_start = nums[i]


        return res