class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dup = []
        for num in nums:
            target = abs(num) - 1
            if nums[target] < 0:
                dup.append(abs(num))
            else:
                nums[target] *= -1

        return dup