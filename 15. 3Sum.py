class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j,k= i+1,len(nums)-1

            while j<k:
                curr = nums[i]+nums[j]+nums[k]

                if curr == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    
                    # Move the k pointer to the j and skip duplicates
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    
                    # Move both pointers after finding a valid triplet
                    j += 1
                    k -= 1
                elif curr<0:
                    j+=1
                else:
                    k-=1

        return res
