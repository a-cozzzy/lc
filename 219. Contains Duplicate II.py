class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictt = {}
        for i, num in enumerate(nums):
            if num in dictt and i-dictt[num]<=k:
                return True
            dictt[num] = i
        return False
            
        