class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check = "".join([char.lower() for char in s if char.isalnum()])

        return check == check[::-1]
        
        