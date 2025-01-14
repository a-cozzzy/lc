class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        n=len(s)
        for i in range(n):
            curr= translations[s[i]]
            if i<n-1 and curr< translations[s[i+1]]:
                result-=curr
            else:
                result+=curr
        return result 
        