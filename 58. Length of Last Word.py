class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip()

        n=len(s)-1
        count=0
        while n >= 0 and (s[n]!=' '):
            count+=1
            n-=1

        return count
        