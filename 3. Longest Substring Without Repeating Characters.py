
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxi=0
        window=set()

        left = 0

        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left+=1

            window.add(s[right])
            maxi=max(maxi,right-left+1)
        return maxi


