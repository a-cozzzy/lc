from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Compare the frequency count of characters in both strings
        return Counter(s) == Counter(t)
