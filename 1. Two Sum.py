class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]x
        """
        new_dict={}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in new_dict:
                return [new_dict[comp],i]
            new_dict[num] = i
        return None