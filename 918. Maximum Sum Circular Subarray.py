class Solution(object):
    def maxSubarraySumCircular(self, nums):
        if not nums:
            return 0

        current_max = nums[0]
        global_max = nums[0]

        current_min = nums[0]
        global_min = nums[0]

        total_sum = sum(nums)

        for i in range(1, len(nums)):
            num = nums[i]
            current_max = max(num, current_max + num)
            global_max = max(global_max, current_max)

            current_min = min(num, current_min + num)
            global_min = min(global_min, current_min)

        if global_max < 0:
            return global_max
        else:
            return max(global_max, total_sum - global_min)  